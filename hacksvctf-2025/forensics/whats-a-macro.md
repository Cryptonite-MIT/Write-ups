**Flag:** `hacks{y0u_f0unD_M3}`

Unzipping the `.pptm` file, we find a bunch of "macros" in a folder all containing "Not the flag!" but one

```bash
.../file.pptm/ppt/slideMasters/_rels $ fd . -t f -X du -b | grep -v '^12'
57      ./maliciousMacroDetails752/macro.vba
```

The flag is there, hex encoded.

```bash
.../file.pptm/ppt/slideMasters/_rels $ cat ./maliciousMacroDetails752/macro.vba | unhex
hacks{y0u_f0unD_M3}
```

