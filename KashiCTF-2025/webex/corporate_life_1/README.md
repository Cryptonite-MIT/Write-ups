# Corporate Life 1

Domain: webex

Points: 137

Solves: 144

### Given information

> The Request Management App is used to view all pending requests for each user. It’s a pretty basic website, though I heard they were working on something new. Anyway, did you know that one of the disgruntled employees shared some company secrets on the Requests Management App, but it's status was set denied before I could see it. Please find out what it was and spill the tea! This Challenge unlocks another challenge in this Series

### Solution

This challenge presented a NextJS website with a static frontend and API route `/api/list`. Upon browsing the website's source code, we find the hidden endpoint `/v2-testing` which uses the `/api/list-v2` endpoint to receive records. This new endpoint filters based on user input passed through the `filter` attribute sent via the JSON body, which is found to be vulnerable to SQL injection as shown in [solve.py](solve.py).
