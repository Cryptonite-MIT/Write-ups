# SNOWy Evening

Domain: Miscellaneous

Points: 205

Solves: 130

### Given information

> A friend of mine , Aakash has gone missing and the only thing we found is this poem...Weirdly, he had a habit of keeping his name as the password.

### Solution

Writeup author: teayah

The title suggests the poem uses *snow steganography* which is a form of whitespace steganography (where ASCII messages are concealed with whitespaces added to the ends of lines) and could be decoded with **stegsnow** and the password is his name: 
```
$ stegsnow -C -p "Aakash" poemm.txt
```
You then get a Pastebin link: [https://pastebin.com/HVQfa14Z](https://pastebin.com/HVQfa14Z)

Here, Mooooooo.txt is a program in COW, an esoteric programming language. It can be decoded with [https://frank-buss.de/cow.html](https://frank-buss.de/cow.html "https://frank-buss.de/cow.html")

**Flag: `KashiCTF{Love_Hurts_5734b5f}`**
