# Key Exchange

Domain: Crypto

Points: 384

Solves: 82

### Given information

> Someone wants to send you a message. But they want something from you first.
```python
from redacted import EllipticCurve, FLAG, EXIT
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib
import random
import json
import os

def encrypt_flag(shared_secret: int):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode("ascii"))
    key = sha1.digest()[:16]
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(FLAG, 16))
    data = {}
    data["iv"] = iv.hex()
    data["ciphertext"] = ciphertext.hex()
    return json.dumps(data)

#Curve Parameters (NIST P-384)
p = 39402006196394479212279040100143613805079739270465446667948293404245721771496870329047266088258938001861606973112319
a = -3
b = 27580193559959705877849011840389048093056905856361568521428707301988689241309860865136260764883745107765439761230575
E = EllipticCurve(p,a,b)
G = E.point(26247035095799689268623156744566981891852923491109213387815615900925518854738050089022388053975719786650872476732087,8325710961489029985546751289520108179287853048861315594709205902480503199884419224438643760392947333078086511627871)

n_A = random.randint(2, p-1)
P_A = n_A * G

print(f"\nReceived from Weierstrass:")
print(f"   Here are the curve parameters (NIST P-384)")
print(f"   {p = }")
print(f"   {a = }")
print(f"   {b = }")
print(f"   And my Public Key: {P_A}")

print(f"\nSend to Weierstrass:")
P_B_x = int(input("   Public Key x-coord: "))
P_B_y = int(input("   Public Key y-coord: "))

try:
    P_B = E.point(P_B_x, P_B_y)
except:
    EXIT()

S = n_A * P_B

print(f"\nReceived from Weierstrass:")
print(f"   Message: {encrypt_flag(S.x)}")

```


### Solution

Writeup author: ph1sh3rm4n

So what this code does is :-  
- Generates private key n_A and public key P_A = n_A * G

- Accepts any valid curve point as your public key P_B

- Computes shared secret S = n_A * P_B and uses S.x for AES encryption of the flag.

This is just a basic `ECDH` MITM challenge.  
So what I did was leverage the server's lack of public key validation by forcing a known secret via the base point G.  
So I send the generator coordinates as the public x and y coordinates.  
```
Public Key x-coord: 26247035095799689268623156744566981891852923491109213387815615900925518854738050089022388053975719786650872476732087  
Public Key y-coord: 8325710961489029985546751289520108179287853048861315594709205902480503199884419224438643760392947333078086511627871
```
Doing so makes the `x-coord` of `P_A` the `shared_secret` cuz  
`shared_secret = n_A * G = P_A`

All's been done now, all that is left to do is to decrypt the `AES-CBC` encryption using the received `iv`, `ct` and our `"publically exposed" shared_secret i.e x-coord of P_A`.  
Here is the `python` code to do so.


```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib
import json

shared_secret_x = 16146798125235834549416451682146277968987439448396610545042225274264745582475246996558006773777661927471315718343272


encrypted_data = '{"iv": "f13be6bd83094fa6a6e7c97b0c8bd05d", "ciphertext": "7be17abaf5e13f1dd7bffa9e8302229cb785507bc84af78acc0faae2a26de3bf45941303b532ea89104b26d4aae28fcbe8a40b3bad2c98afcb5f31445ffb19f847dbf35c16e4db1c5f83341ade3d9e0b1a9cc60c83ad9de8107b4cc534377e57"}'


shared_secret_str = str(shared_secret_x)
sha1 = hashlib.sha1(shared_secret_str.encode("utf-8")).digest()
key = sha1[:16]  


data = json.loads(encrypted_data)
iv = bytes.fromhex(data["iv"])
ciphertext = bytes.fromhex(data["ciphertext"])

cipher = AES.new(key, AES.MODE_CBC, iv)

plaintext = unpad(cipher.decrypt(ciphertext), 16)
print("Flag:", plaintext.decode())
```
After decryption, we get this :-
```
NaeusGRX{L_r3H3Nv3h_kq_Sun1Vm_O3w_4fg_4lx_1_t0d_a4q_lk1s_X0hcc_Dd4J_sAE7Vfb8}

Hint: DamnKeys
```
This was straight up Vignere Cipher.  
I opened up `CyberChef` and decoded the encrypted flag with the key `DamnKeys` and voila, we get our flag!

> FLAG -> KashiCTF{I_r3V3Al3d_my_Pub1Ic_K3y_4nd_4ll_1_g0t_w4s_th1s_L0usy_Fl4G_sOR7Lbd8}
