First we run `binwalk -eaM` on `flag_1_1` to find a ppt with 3 images.

In `image3.png` we find a hidden message in the metadata.

```
Artist                          : #                                                                                                        #
```

We convert the `0x20` to `0` and `0xe28083` to `1` to get the flag.
