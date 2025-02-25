# Leap Of Faith

Domain: PWN

Points: 463

Solves: 47

### Given information

> I liked playing Super Mario just for jumping from one place to another. Can you do that?

### Recon

In the given challenge we are prompted to enter one address where we wish to jump to, after which it finish executing.
There's a win function which checks the argument passed, if the conditions are satisfied, it open a flag and prints the content, below is the pseudocode

```c
void win(int param_1,int param_2,int param_3)

{
  char *pcVar1;
  char local_78 [104];
  FILE *local_10;
  
  if (((0xde < param_1) && (0xad < param_2)) && (0xc0de < param_3)) {
    local_10 = fopen("/flag.txt","r");
    if (local_10 == (FILE *)0x0) {
      puts("Failed to open file");
                    // WARNING: Subroutine does not return
      exit(1);
    }
    pcVar1 = fgets(local_78,100,local_10);
    if (pcVar1 == (char *)0x0) {
      puts("Failed to read line");
    }
    else {
      printf("flag is : %s",local_78);
    }
    fclose(local_10);
    return;
  }
  printf("Bro where are the arguments ?");
                    // WARNING: Subroutine does not return
  exit(0x45);
}
```

### Exploitation

As you may notice we can simply jump to the line where it opens the flag and skip the argument check, the address for that is `0x4011ba`

However when we do this on nc, we get nothing, The issue lies with fgets, which reads the content of file stream into an local variable, probably due to some stack size issue because the flag size might override the return address.
To remedy that we notice in the disassembly of main

```asm
   0x000000000040125a <+0>:	push   rbp
   0x000000000040125b <+1>:	mov    rbp,rsp
   0x000000000040125e <+4>:	sub    rsp,0x10
   0x0000000000401262 <+8>:	lea    rdi,[rip+0xdff]        # 0x402068
   0x0000000000401269 <+15>:	mov    eax,0x0
   0x000000000040126e <+20>:	call   0x401050 <printf@plt>
   0x0000000000401273 <+25>:	lea    rax,[rbp-0x8]
   0x0000000000401277 <+29>:	mov    rsi,rax
   0x000000000040127a <+32>:	lea    rdi,[rip+0xe27]        # 0x4020a8
   0x0000000000401281 <+39>:	mov    eax,0x0
   0x0000000000401286 <+44>:	call   0x401080 <__isoc99_scanf@plt>
   0x000000000040128b <+49>:	mov    rax,QWORD PTR [rbp-0x8]
   0x000000000040128f <+53>:	sub    rsp,0x10
   0x0000000000401293 <+57>:	jmp    rax
   0x0000000000401295 <+59>:	mov    eax,0x0
   0x000000000040129a <+64>:	leave
   0x000000000040129b <+65>:	ret
```

we can jump to `0x40125e` where it does `sub rsp,0x10` and continue executing the instructions till it asks for an address to jump to again.

This could be used to increase the stack size for the flag to fit.
By making a script which bruteforces the number of times we might have to jump to `0x40125e` instruction and finally jump to `0x4011ba` to get the flag

[The solve script](solve.py)

 

