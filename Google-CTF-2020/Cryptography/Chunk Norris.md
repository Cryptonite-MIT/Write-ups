# Chunk Norris

This was the easy crypto challenge in this year's Google CTF. It is basically an RSA cryptosystem with a custom prime generation.

## Challenge
```
Chunk Norris is black belt in fast random number generation
```
### Solved by: TheBlueFlame121
#### Points: 111

```py
import random
from Crypto.Util.number import *
import gmpy2

a = 0xe64a5f84e2762be5
chunk_size = 64

def gen_prime(bits):
  s = random.getrandbits(chunk_size)

  while True:
    s |= 0xc000000000000001
    p = 0
    for _ in range(bits // chunk_size):
      p = (p << chunk_size) + s
      s = a * s % 2**chunk_size
    if gmpy2.is_prime(p):
      return p

n = gen_prime(1024) * gen_prime(1024)
e = 65537
flag = open("flag.txt", "rb").read()
print('n =', hex(n))
print('e =', hex(e))
print('c =', hex(pow(bytes_to_long(flag), e, n)))
```
Output:
>n = 0xab802dca026b18251449baece42ba2162bf1f8f5dda60da5f8baef3e5dd49d155c1701a21c2bd5dfee142fd3a240f429878c8d4402f5c4c7f4bc630c74a4d263db3674669a18c9a7f5018c2f32cb4732acf448c95de86fcd6f312287cebff378125f12458932722ca2f1a891f319ec672da65ea03d0e74e7b601a04435598e2994423362ec605ef5968456970cb367f6b6e55f9d713d82f89aca0b633e7643ddb0ec263dc29f0946cfc28ccbf8e65c2da1b67b18a3fbc8cee3305a25841dfa31990f9aab219c85a2149e51dff2ab7e0989a50d988ca9ccdce34892eb27686fa985f96061620e6902e42bdd00d2768b14a9eb39b3feee51e80273d3d4255f6b19
e = 0x10001
c = 0x6a12d56e26e460f456102c83c68b5cf355b2e57d5b176b32658d07619ce8e542d927bbea12fb8f90d7a1922fe68077af0f3794bfd26e7d560031c7c9238198685ad9ef1ac1966da39936b33c7bb00bdb13bec27b23f87028e99fdea0fbee4df721fd487d491e9d3087e986a79106f9d6f5431522270200c5d545d19df446dee6baa3051be6332ad7e4e6f44260b1594ec8a588c0450bcc8f23abb0121bcabf7551fd0ec11cd61c55ea89ae5d9bcc91f46b39d84f808562a42bb87a8854373b234e71fe6688021672c271c22aad0887304f7dd2b5f77136271a571591c48f438e6f1c08ed65d0088da562e0d8ae2dadd1234e72a40141429f5746d2d41452d916

### Solution
We can essentially reduce the generation function to:
```py
def gen_prime(bits, s):
    p = 0
    for _ in range(bits // chunk_size):
        p = (p << chunk_size) + s
        s = a * s % 2**chunk_size
    return p
```

So all it boils down to is finding the s value of both the primes and we can break the modulus and hence the RSA. From the generation function, we can write the equation of the primes as:

<img src="https://render.githubusercontent.com/render/math?math=P = s .{2^{960}} + (as \mod {2^{64}})*2^{896} + ...... + (a^{14}s \mod 2^{64})*2^{64} + (a^{15}s \mod 2^{64}))">

So if we can get the s values for both of the primes, we can break the encryption!. Let the primes be <img src="https://render.githubusercontent.com/render/math?math=p"> and <img src="https://render.githubusercontent.com/render/math?math=q"> and let the s values for them be <img src="https://render.githubusercontent.com/render/math?math=s_1"> and <img src="https://render.githubusercontent.com/render/math?math=s_2"> respectively.

If we look at the equation for <img src="https://render.githubusercontent.com/render/math?math=n">, we can see the 64 MSB bits will be a result of the multiplication of the first term's MSB bits. Similarly the 64 LSB bits will be the result of the product last term's LSB bits. Using these two relation we can basically get the value of <img src="https://render.githubusercontent.com/render/math?math=s_1 * s_2"> and then it's just a matter of bruteforcing over it's divisors.

<img src="https://render.githubusercontent.com/render/math?math=64 LSB \ bits \equiv [(a^{15}s_1 \mod  2^{64})*(a^{15}s_2 \mod 2^{64}) ]\mod 2^{64} \equiv a^{30}s_1s_2 \mod 2^{64}">

<img src="https://render.githubusercontent.com/render/math?math=64 MSB \ bits = s_1*s_2">

So here's the full implementaion in sage:
```py
import gmpy2
from Crypto.Util.number import *

def gen_prime(bits, s):
    p = 0
    for _ in range(bits // chunk_size):
        p = (p << chunk_size) + s
        s = a * s % 2**chunk_size
    return p
    
prod1 = Integer(pow(a, -30, 2**65)*n % 2**65)    #modulus is 64 bits cause we need 64 bits
prod2 = n >> (2048 - 64)
s1s2 = (prod2 -1)*(2**64) + prod1    #prod2 - 1 to take care of the overflow caused by other terms

for d in divisors:
    p = gen_prime(1024, d)
    g = gcd(n, p)
    if g != 1:
        print(p)
        break
        
q = n//p
d = inverse_mod(0x10001, (p-1)*(q-1))
print(long_to_bytes(pow(c, d, n)).decode())
```

### Flag
`CTF{__donald_knuths_lcg_would_be_better_well_i_dont_think_s0__}`

---
