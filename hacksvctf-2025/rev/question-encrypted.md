```
31c050682a6f2e6768292b2b456829452f72686e452e726869617d2968727b7971b9180000008
d342489e7ac341aaae2fab804000000bb0100000089e1ba18000000cd80b80100000031dbcd80
```

This looks like a shellcode so I put this into a bin file and used ndiasm to disassemble this 

```
❯ ndisasm -b 32 ./shellcode.bin
00000000  31C0              xor eax,eax
00000002  50                push eax
00000003  682A6F2E67        push dword 0x672e6f2a
00000008  68292B2B45        push dword 0x452b2b29
0000000D  6829452F72        push dword 0x722f4529
00000012  686E452E72        push dword 0x722e456e
00000017  6869617D29        push dword 0x297d6169
0000001C  68727B7971        push dword 0x71797b72
00000021  B918000000        mov ecx,0x18
00000026  8D3424            lea esi,[esp]
00000029  89E7              mov edi,esp
0000002B  AC                lodsb
0000002C  341A              xor al,0x1a
0000002E  AA                stosb
0000002F  E2FA              loop 0x2b
00000031  B804000000        mov eax,0x4
00000036  BB01000000        mov ebx,0x1
0000003B  89E1              mov ecx,esp
0000003D  BA18000000        mov edx,0x18
00000042  CD80              int 0x80
00000044  B801000000        mov eax,0x1
00000049  31DB              xor ebx,ebx
0000004B  CD80              int 0x80
❯
```

This is just a xor operation with key 0x1a

I used cyberchef to reverse it 

`hacks{g33_5h311_0u4}`
