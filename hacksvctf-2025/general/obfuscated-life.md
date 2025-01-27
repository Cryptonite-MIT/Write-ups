**Flag:** `hacks{don't_be_a_obfuscated_nerd}`

The JS code is obfuscated using https://obf-io.deobfuscate.io/.

Deobfuscating it, we get the flag in the code.

```js
function hi() {
  if (document.domain == "obfuscator.io") {
    console.log("hacks{don't_be_a_obfuscated_nerd}");
  }
  console.log("Hmmmm I wonder where the flag is?");
}
hi();
```
