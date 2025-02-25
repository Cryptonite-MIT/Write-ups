# Random-Inator

Domain: Cryptography

Points: 476

Solves: 38

### Given information

> Dr. Heinz Doofenshmirtz plans to take over the Tri-State Area. He created this super secret uncrackable encryption program with the help of his robot buttler Norm. Help Perry the Platypus decrypt the message and sabotage his evil plans.

```python
from redacted import PRNG, FLAG
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt(key, plaintext, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, 16))
    return iv+ciphertext

P = PRNG()
KEY = P.getBytes(16)
IV = P.getBytes(16)

print(f"Doofenshmirtz Evil Incorporated!!!\n")
print(f"All right, I don't like to repeat myself here but it just happens\nAnyhow, here's the encrypted message: {encrypt(KEY, FLAG, IV).hex()}\nOhh, How I love EVIL")
while True:
    iv = P.getBytes(16) 
    try:
        pt = input("\nPlaintext >> ")
        pt = bytes.fromhex(pt)
    except KeyboardInterrupt:
        break
    except:
        print("Invalid input")
        continue

    ct = encrypt(KEY, pt, iv)
    print(ct.hex())
```

### Solution

Writeup author: goosbo

The `encrypt` function encrypts the plaintext with `AES` in `CBC` mode and returns the `iv` concatenated with the ciphertext. 

The code randomly generates the 16 byte `KEY` and `IV` with a prng and uses it to encrypt the flag. 

It lets the user input plaintexts and it encrypts them with the same key used for the flag but the iv is generated using the prng.

Since we are given the encrypted message of the flag, we can extract `IV` and ciphertext. If the `prng` used is predictable, it is possible to retrieve the key used for flag encryption.

Made a script to continuously enter plaintexts and extract the iv each time. The scripts prints the unique `iv`s generated.
 ```python
from pwn import *

HOST = 'kashictf.iitbhucybersec.in'
PORT = 61474

r = remote(HOST,PORT)

rands = set()
for i in range(100):
    r.recvuntil('Plaintext >> ')
    r.sendline('00')
    a = r.recvline().decode()
    rands.add(bytearray.fromhex(a)[:16].hex())
    print(i)

print(rands)
```

On generating 100 random iv's only 10 unique ones are found.
```
['f6a9d2852e5c9c5e249188bd32776866', '5b757cc3fe4d1d51ece7f972421ca89d', '674d8fb80bce301e336476b1dd4ef695', '5d03b39ad3d949e73d297734a9f84b72', '7aba152e75735bc86567d804294acc82', '963483730151eb82840db14f17159c66', 'da4f91417cc40c722bea594809044f3d', 'a221a2e491207cf23f755e9cbc052de8', '6be0323ac7b2f98edc19907467950a36', 'b375293656a8b9f32b6789eff95003d1']
```

Looped through each of these as the key and tried to decrypt the ciphertext with it and the `IV` that was already found.
```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
rands = ['f6a9d2852e5c9c5e249188bd32776866', '5b757cc3fe4d1d51ece7f972421ca89d', '674d8fb80bce301e336476b1dd4ef695', '5d03b39ad3d949e73d297734a9f84b72', '7aba152e75735bc86567d804294acc82', '963483730151eb82840db14f17159c66', 'da4f91417cc40c722bea594809044f3d', 'a221a2e491207cf23f755e9cbc052de8', '6be0323ac7b2f98edc19907467950a36', 'b375293656a8b9f32b6789eff95003d1']
encrypted = bytearray.fromhex('da4f91417cc40c722bea594809044f3d2daaf555bdd18568fc050e8f6f4a70a4d36a58d45be7c745bba3d29beed7dd0346616e4896e033e6942726153753b9443cd574fbcd8e74a56be696a0062da11ac5fc5d4e422b7c635cd4dfc95951589d')

iv = encrypted[:16]
ciphertext = encrypted[16:]

for k in rands:
    aes = AES.new(bytes.fromhex(k),mode=AES.MODE_CBC,iv=iv)
    decoded = aes.decrypt(ciphertext)
    if 'KashiCTF'.encode() in decoded:
        print(decoded)
```
Output:
```
b'KashiCTF{Y0u_brOK3_mY_R4Nd0m_In4t0r_Curse_yOu_Perry_tH3_Pl4TYpus_x4DvQAdz}\x06\x06\x06\x06\x06\x06'
```

Flag: `KashiCTF{Y0u_brOK3_mY_R4Nd0m_In4t0r_Curse_yOu_Perry_tH3_Pl4TYpus_x4DvQAdz}`