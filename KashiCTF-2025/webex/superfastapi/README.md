# SuperFastAPI

Domain: webex

Points: 100

Solves: 209

### Given information

> Made my verty first API! However I have to still integrate it with a frontend so can't do much at this point lol.

### Solution

FastAPI's [default Swagger `/docs` endpoint](https://fastapi.tiangolo.com/tutorial/metadata/#docs-urls) gives us all the API routes. We are able to `GET /flag/{username}` the flag after setting the `role` as `admin` using the `PUT /get/{username}` route.

[solve.py](solve.py)
