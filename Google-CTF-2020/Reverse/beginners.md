### Beginner

We are asked to enter the flag through stdin.

When we look at the disassembly, we can observe that 
our input is first copied into the xmm0 register and 
then it is transformed using the following instructions.

```
pshufb  xmm0, cs:SHUFFLE; 
paddd   xmm0, cs:ADD32
pxor    xmm0, cs:XOR
```

Here are the constants used for the SIMD 
insructions with LSB towards the right.

```
SHUFFLE        02 06 07 01 05 0B 09 0E 03 0F 04 08 0A 0C 0D
ADD         EF BE AD DE AD DE E1 FE 37 13 37 13 66 74 63 67
XOR         76 58 B4 49 8D 1A 5F 38 D4 23 F8 34 EB 86 F9 AA
```

Once the input has been transformed, it is checked
against the original form and equal, we succeed.


Our string is first shuffled then added and xored
according to the above data. We also know that the
flag expects a prefix of `CTF{`. So from here it is
easy to reverse the flag. I first tried automating
it using constraint solvers, but I wasn't able to,
so I just went character by character.

XOR

```
<-- CTF{??????????}\0
43 54 46 7B  ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 7D 00
76 58 B4 49 8D 1A 5F 38 D4 23 F8 34 EB 86 F9 AA
---
35 0C F2 32  ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 84 AA
```

ADD

```
35 0C F2 32  ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 84 AA
EF BE AD DE AD DE E1 FE 37 13 37 13 66 74 63 67
---
46 4D 45 54  ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 21 43
```

SHUFFLE

```
46 4D 45 54  ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 21 43
02 06 07 01 05 0B 09 0E 03 0F 04 08 0A 0C 0D
---
43 54 46  ?  ?  ? 4D 45  ?  ?  ?  ?  ? 21  ?  ?
--> CTF{??ME?????!}\0
```

Now we can look at the known characters and apply
the reverse transformations to get other characters.
As an example, if we look at `{` in the result above,
we can see that it came from position 8 so we can get
the character at position 8 by running the following
python script:

```python
import string

for i in range(256):
    if( ((i^0x37) - 0xD4) & 0xff == ord('}')):
        print(chr(i), hex(i))
```

I also had to take care of some off-by-one errors
due to the overflow during add. `CTF{S1MDf0rM3!}`

