# Easy Jail 2

Domain: misc

Points: 100

Solves: 195

### Given information

> I made a completely secure calculator this time.

### Solution

Writeup Author: BlueKnight2345

UTF-8 keywords like `open`, `globals` etc. are blocked. We resort to Unicode Homoglyphs to bypass this blacklist:

```
𝚘𝚙𝚎𝚗("/flag.txt").read()  # Unicode characters
```

`𝚘` (U+1D670) instead of `o`

`𝚙` (U+1D671) instead of `p`

`𝚎` (U+1D672) instead of `e`

`𝚗` (U+1D673) instead of `n`

flag: `KashiCTF{C4N_S71LL_CL3AR_8L4CKL15T_55tvKYt9}`
