# Not Suspicious Agency

## Description
The Not Suspicous Agency has created a very secure way to encrypt your messages that only trusted individuals can decrypt. Trust is very important after all.

## Solution
Reference for Dual_EC_DRBG:
https://www.youtube.com/watch?v=nybVFJVXbww <br><br>
`P` and `Q` are  nistp256 points. `e` referenced in the video is what we have in `backdoor.txt`. We can check that `Q = eP`. So, we recover `rQ` by bruteforce, and multiply it by inverse of `e` to get the state `s`. <br><br>
```einv * (r * Q) = einv * (r * e * P) = einv * e * (rP) = rP and s = rP.x```
<br><br>

```py
def find_y_square(x):
    a = 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc
    b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
    y2 = (pow(x, 3, p) + a * x + b) % p
    return y2

e = 106285652031011072675634249779849270405
n = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551
p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff

trunc_rQ = strxor(test_op, test_str)[:30]

flag = False
for i in range (256):
    for j in range (256):
        b1 = long_to_bytes(i)
        b2 = long_to_bytes(j)
        rQx = bytes_to_long(b1 + b2 + trunc_rQ)
        ysq = int(find_y_square(int(rQx)))
        try:
            y = pow(ysq, (p + 1) // 4, p)
            Z = ECC.EccPoint(rQx, y, curve='p256')
            einv = pow(e, -1, n)
            rP = einv * Z
            s2 = int(rP.x)
            g2 = generate(P, Q, s2)
            pt = encrypt(g2, test_op[-5:])
            if pt == b'gging':
                print(pt)
                pt = encrypt(g2, flag_op)
                print(pt)
                flag = True
        except:
            pass
        if flag:
            break
    if flag:
        break
if not flag:
    print("not found")
```

## Flag
`BITSCTF{N3V3r_811ND1Y_7rU57_574ND4rD5}`
