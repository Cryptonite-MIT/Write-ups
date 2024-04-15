# Drug Injection

Domain: Web

Points: 300

Solves: 32

### Given information

> I made a Drug awareness website for my Drug Addict friend as a joke to help him get over his addiction. He kept complaining about not being able to login. He Scored an injection drug. I tried to convince him that he should stop getting High before he tries to login. injections won't always help u to get HIGHer access. He was not satisfied with just a single injection, he wanted to try Double Dose. How do I convince him to stop. Help me spread awareness.

### Solution

The login form at `/login.php` was found to be vulnerable to SQL injection with the username `admin` and password `' or 1=1-- -`. Nothing useful was found at the landing page `/welcome.php`. Hence we try to look into the database.

In case of any error in SQL query all we get is `Login failed. Please check your username and password.` hence this is a blind SQL challenge. We find the flag in the admin's password after using the `SUBSTR` function to extract it character by character using this payload:

```sql
' UNION SELECT username,1,1,1 FROM users WHERE username='admin' AND substr(password, {<substr_idx>}, 1) = '{<character>}'-- -
```

[solve.py](solve.py)

Note: The `LIKE` operator can also be used here but it could cause issues as:
- `_` is a `LIKE` wildcard for any single character and hence presents problems if present in the actual flag
- sqlite3's `LIKE` is case-insensitive
