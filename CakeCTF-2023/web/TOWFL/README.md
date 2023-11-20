Challenge name: TOWFL

Category: Web

Solves: 171

### Given information

> Do you speak the language of wolves?

> Prove your skill [here](http://towfl.2023.cakectf.com:8888/)!

### Solution

This challenge involves an online test website with a Flask backend. Hundred lorem-ipsum MCQ type questions are generated whose answers are random. The flag is revealed if and only if the player gets all the questions right. P(100 points doing it manually) = 0.25^100. So we can't go manual.
repeatedly get the same set of questions with the same correct answers

```
@app.route("/api/score", methods=['GET'])
def api_score():
    if 'eid' not in flask.session:
        return {'status': 'error', 'reason': 'Exam has not started yet.'}

    # Calculate score
    challs = json.loads(db().get(flask.session['eid']))
    score = 0
    for chall in challs:
        for result in chall['results']:
            if result is True:
                score += 1

    # Is he/she worth giving the flag?
    if score == 100:
        flag = os.getenv("FLAG")
    else:
        flag = "Get perfect score for flag"

    # Prevent reply attack
    flask.session.clear() # SESSION NEVER ACTUALLY GETS DESTROYED if this is used

    return {'status': 'ok', 'data': {'score': score, 'flag': flag}}
```

`flask.session.clear()` seems to be preventing a replay attack by invalidating the session cookie but in reality all it's doing is deleting the session cookie at client side. The session forever lives on server side.

Hence even after visiting the `/api/submit` endpoint (where the `flask.session.clear()` method gets called) we can continue to use the (theoretically invalid) session cookie to validate our answers. We would repeatedly get the same set of questions with the same correct answers, thus we will end up getting a perfect score after a worst case scenario of 400 tries.

[solve.py](solve.py)

---

### References

-   https://stackoverflow.com/a/21083908

-   Flask replay attack prevention: https://stackoverflow.com/a/30851749
