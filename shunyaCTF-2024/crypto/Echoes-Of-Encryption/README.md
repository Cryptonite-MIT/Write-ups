# Echoes-Of-Encryption


Domain : Cryptography

Points : 200

Solves : 35


### Given information

> In December 2022, my friend Alok's device was hacked. Upon investigation, he discovered that the breach was due to a vulnerability in the Nvidia SMC which had been recently discovered and published for research purposes on the same day he was hacked.<br><br>PS- In the end, only numbers matter to grow a plant from a seed!!


### Solution

On going through the attached `encrypt.py`, we can see that a key is being randomly generated based on a seed.
After which it performs xor between the flag and the generated key.
So If we can get the key and xor it with the given encrypted hex, challenge solved.

On reading the description of the challenge these words stood out
```
the breach was due to a vulnerability in the Nvidia SMC which had been recently discovered and published for research purposes on the same day he was hacked
```

I figured this hinted to the seed to generate the key.
Sure enough, looked up nvidia smc vuln December 2022 and reached this : https://nvd.nist.gov/vuln/detail/CVE-2022-42269 \
`CVE-2022-42269`

The seed was the cve number with the year `202242269`


Solve script:

```python
import random
import string

def decrypt_string(input_string, seed):
    random.seed(seed)
    
    encrypted_string = bytes.fromhex(input_string)


    allowed_chars = string.ascii_letters + string.digits
    key = ''.join(random.choices(allowed_chars, k=len(input_string)//2))
    
    flag = ''
    
    for i in range(len(encrypted_string)):
        decrypted_char = chr(encrypted_string[i] ^ ord(key[i]))
        flag += decrypted_char
    return flag


seed_value = 202242269
input_string = "5e04610a22042638723c571e1a5436142764061f39176b4414204636251072220a35583a60234d2d28082b"
decrypted = decrypt_string(input_string, seed_value)
print(decrypted)
```


### Flag 

`0CTF{alw4y5_r3ad_7he_d3scr!pti0n_c4r3fully}`


