# You Should Rev This 

Domain: Rev

Points: 499

Solves: 10

### Given information

> Did you know that the x86 mov instruction is turing complete?

### Solution

Writeup author: arikazo

The executable only consists of mov instruction \
It was probably obfuscated using [`movffuscator`](https://github.com/xoreaxeaxeax/movfuscator)

Disassembled the binary in cutter and found these strings
```
0x08050040 /flag.txt
0x0805004a nope\n
0x08050050 Got input: '%s'\n
0x08050061 Enter the password: 
0x08050076 e1n5tds4bu4et1n4ui2oh2ou4s4tu2o
0x08050096 error opening flag
```
Found the instructions that was loading the string `Enter the password:`
The instruction that is reading the password from stdin must be around this instruction

```
0x0804bbc0      mov     eax, str.Enter_the_password: ; 0x8050061
```

Scrolled a bit around this instruction and found the part that read the flag (I think)

```
0x0804d77e      mov     eax, str.flag.txt ; section..data
                                   ; 0x8050040
0x0804d783      mov     dword [R3], eax ; 0x80500bc
0x0804d788      mov     eax, dword [R3] ; 0x80500bc
```

After that i could not understand what was happening 

So i started finding some tool that could deobsfuscate this and i found this \
[`demovfuscator`](https://github.com/leetonidas/demovfuscator)

Unfortunately i could not run this locally but there is a
[`docker image`](https://hub.docker.com/r/iyzyi/demovfuscator) for this 
,which i found from this [`writeup`](https://ctftime.org/writeup/38965)

Then i used all the commands from the demovfuscator tool and got three things
1. A binary that replaced some mov instruction with other instruction but it was still heavily obfuscated
2. A png file that showed all the possible branches but it did not help
3. A symbols.idc file which was also not helpful 


After some more googling i found another [`writeup`](https://guyinatuxedo.github.io/22-movfuscation/recon_movfuscated/index.html) that had the script to solve a challenge like this 

The solution in this writeup checked how many instruction was getting executed every time a letter was sent 

If the letter is correct then it will move on to the next letter and so on. \
So each time a correct letter is guessed, the number of instructions getting executed is increased. \
If the number of execution increased from last time then that means the latest letter sent is correct so it appends that letter to the password. 

[solve.py](solve.py)

**Flag:** `KashiCTF{d1d_y0u_r3v_17_b4J8wzU4j}`
