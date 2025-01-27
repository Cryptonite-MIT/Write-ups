**Flag:** `hacks{ijijkijkkji}`

We're given a file with both whitespace (WS) language and JavaScript code

```js
  i=String.

  fromCharCode   (    9)
;
 j=String
.fromCharCode(32)
    ;   k=
String


     .fromCharCode
(10);

console.

log

("i="

+i+

"j="

+j+"k="

+

k);










```

Putting it through a WS interpreter, we get the following output:

```
push 104
push 97
push 99
push 107
push 115
push 123
push 9
push 32
push 9
push 32
push 10
push 9
push 32
push 10
push 10
push 32
push 9
push 125
```

We also know that `i` is a tab, `j` is a space, and `k` is a newline.

Putting it together, we get the flag.

