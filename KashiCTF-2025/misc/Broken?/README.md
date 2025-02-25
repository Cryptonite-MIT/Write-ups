# Broken

Domain: Misc

Points: 490

Solves: 25

### Given information

> You find his laptop lying there and his futile attempt to read a random file..!

### Solution

Writeup author: Wixter_07

We are given chall.py

```py
#!/usr/bin/env python3

import hashlib
import socket
import signal
import sys

HOST = "0.0.0.0"
PORT = 1337
SECRET_KEY = b"REDACTED"

def generate_hmac(message):
    return hashlib.sha1(SECRET_KEY + message.encode()).hexdigest()

def signal_handler(sig, frame):
    print("\n[!] Server shutting down...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def handle_client(client, addr):
    print(f"[*] Connection from {addr}")

    try:
        original_data = "count=10&lat=37.351&user_id=1&long=-119.827&file=random.txt"
        original_hmac = generate_hmac(original_data)

        client.sendall(f"Retrieve file using format: data|hmac\nExample: {original_data}|{original_hmac}\n".encode())

        data = client.recv(1024)
        if not data:
            print(f"[-] Client {addr} disconnected.")
            return

        try:
            decoded_data = data.decode("utf-8").strip()
        except UnicodeDecodeError:
            decoded_data = data.decode("latin-1").strip()

        print(f"[*] Received Data: {decoded_data}")

        if "|" not in decoded_data:
            client.sendall(b"Invalid format. Use data|hmac\n")
            return

        user_data, received_hmac = decoded_data.rsplit("|", 1)

        user_data_bytes = bytes(user_data, "utf-8").decode("unicode_escape").encode("latin-1")

        h = hashlib.sha1()
        h.update(SECRET_KEY + user_data_bytes)
        computed_signature = h.hexdigest()

        print(f"[*] Computed Signature: {computed_signature} for body: {repr(user_data)}")
        print(f"[*] Received Signature: {received_hmac}")

        if computed_signature != received_hmac:
            client.sendall(b"Invalid HMAC. Try again.\n")
        else:
            try:
                params = dict(param.split("=") for param in user_data.split("&") if "=" in param)
                filename = params.get("file")
                if filename:
                    with open(filename, "r") as f:
                        content = f.read()
                    client.sendall(f"File Contents:\n{content}\n".encode())
                else:
                    client.sendall(b"Invalid request format.\n")
            except FileNotFoundError:
                client.sendall(b"File not found.\n")

    except ConnectionResetError:
        print(f"[!] Client {addr} forcibly disconnected.")

    except Exception as e:
        print(f"[!] Error handling client {addr}: {e}")

    finally:
        client.close()
        print(f"[-] Closed connection with {addr}")

def start_server():
    print(f"[*] Listening on {HOST}:{PORT} ...")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)

    while True:
        try:
            client, addr = server.accept()
            handle_client(client, addr)
        except KeyboardInterrupt:
            print("\n[!] Shutting down server...")
            server.close()
            sys.exit(0)

if __name__ == "__main__":
    start_server()

```

So basically the exploit was to perform [hash length extension attack](https://en.wikipedia.org/wiki/Length_extension_attack) as SHA1 is vulnerable to it. We can use this handy tool called [Hash_Extender](https://github.com/eid3t1c/Hash_Extender) as a subprocess.

When we connect to the nc, we are give `<known_message>|<known_message_signature>`. known_message_signature is SHA1 hash of the `SECRET + known_message`. We know that the message and the signature for it is static from chall.py.

Since hash functions use padding to make the message length a multiple of a block size, we can append valid padding, and then append new data without the need of knowing SECRET and still generating a valid signature as if we knew SECRET. We just need to know the length of SECRET.



The nc gives us known_message = `count=10&lat=37.351&user_id=1&long=-119.827&file=random.txt` and known_message_signature = `01be4a249bed4886b93d380daba91eb4a0b1ee29`

We can craft the exploit based on this part from chall.py
```py
            try:
                params = dict(param.split("=") for param in user_data.split("&") if "=" in param)
                filename = params.get("file")
                if filename:
                    with open(filename, "r") as f:
                        content = f.read()
                    client.sendall(f"File Contents:\n{content}\n".encode())
                else:
                    client.sendall(b"Invalid request format.\n")
            except FileNotFoundError:
                client.sendall(b"File not found.\n")
```

So we can append something like `&file=flag.txt` on to the payload and it'd be readout from the server.

Now since we don't know the key length, we need to brute it. I made this script and stored all the payloads as `<new_message>|<new_signature>` in ![brute.txt](brute.txt)

```py
import subprocess


hash_function = "SHA1"
signature = "01be4a249bed4886b93d380daba91eb4a0b1ee29"
data = "count=10&lat=37.351&user_id=1&long=-119.827&file=random.txt"
extension = "&file=flag.txt"
output_file = "brute.txt"

with open(output_file, "w") as f:
    for key_length in range(1, 71):  
        print(f"[*] Testing key length {key_length}")


        result = subprocess.run(
            [
                "python3",
                "Length_Extender.py",
                "-f", hash_function,
                "-s", signature,
                "-d", data,
                "-e", extension,
                "-k", str(key_length)
            ],
            capture_output=True,
            text=True
        )


        output = result.stdout.strip().split("\n")

        new_message, new_signature = None, None

        for line in output:
            if "New Message =" in line:
                new_message = line.split("=", 1)[1].strip()
            if "New Signature =" in line:
                new_signature = line.split("=", 1)[1].strip()

        if new_message and new_signature:


            f.write(f"{new_message}|{new_signature}\n")

print("[+] Brute-force completed. Results saved in brute.txt")
```

We have to send back `<new_message>|<new_signature>` back to the nc.

```py
from pwn import *

HOST = "kashictf.iitbhucybersec.in"
PORT = 

payloads = []

with open("brute.txt", "r") as f:
    for line in f:
        line = line.strip()
        if "|" in line:
            message, signature = line.split("|", 1)
            message = bytes(message, "latin1").decode()
            signature = signature.strip()  
            payloads.append((message, signature))

for i, (message, signature) in enumerate(payloads):
    print(f"[*] Testing payload {i+1}/{len(payloads)}")

    # Debugging: Print the raw payload correctly
    print(f"[*] Sending payload: {message.encode()}|{signature}")

    conn = remote(HOST, PORT, level='DEBUG')

    initial_msg = conn.recv().decode()
    print(f"[*] Server Response: {initial_msg.strip()}")

    full_payload = message.encode() + b"|" + signature.encode()
    conn.sendline(full_payload)

    try:
        response = conn.recv(timeout=3).decode()
        print(f"[*] Response for payload {i+1}: {response.strip()}\n")

        if "File Contents" in response:
            print(f"[+] Success! Found valid payload at index {i+1}:\n{message}")
            with open("valid_payload.txt", "w") as valid_file:
                valid_file.write(message + "|" + signature + "\n")
            break

    except EOFError:
        print(f"[-] Connection closed unexpectedly on payload {i+1}")

    conn.close()
```

The flag - **`KashiCTF{Close_Yet_Far_RmEroVhEJ}`**
