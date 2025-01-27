**Flag:** `hacks{sstv_r0cks}`

The flag is encoded using base64 SSTV (Slow Scan Television) in the audio file.

Decoding it gives us the flag.

```bash
$ sstv -d *wav -o res.png
```

