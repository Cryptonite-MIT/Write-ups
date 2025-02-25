# Memories Bring Back You

Domain: Forensics

Points: 100

Solves: 258

### Given information

> A collection of images, a digital time capsule—preserved in this file. But is every picture really just a picture? A photographer once said, “Every image tells a story, but some stories are meant to stay hidden.” Maybe it’s time to inspect the unseen and find what’s been left behind.

### Solution

Writeup author: taci

We can see that the file is a disk image or a memory boot containg a `Master Boot Record (MBR)`. Running `mmls` on it we can see that there is a `NTFS/exFAT partition` at `Sector 128 - 2041983`. 
```
file memory
memory: DOS/MBR boot sector MS-MBR Windows 7 english at offset 0x163 "Invalid partition table" at offset 0x17b "Error loading operating system" at offset 0x19a "Missing operating system", disk signature 0x5032578b; partition 1 : ID=0x7, start-CHS (0x0,2,3), end-CHS (0x7e,254,63), startsector 128, 2041856 sectors
mmls memory
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000000127   0000000128   Unallocated
002:  000:000   0000000128   0002041983   0002041856   NTFS / exFAT (0x07)
003:  -------   0002041984   0002047999   0000006016   Unallocated
```

So we can explore the files inside this partition by mounting it.
```
sudo mount -o loop,ro,offset=$((128*512)) memory /mnt
cd /mnt
```

Now listing the files we can see a bunch of images as well as a `flag.txt`. So we can do `cat flag.txt` to read the flag.
```
cat flag.txt
��KashiCTF{Not_so_easy}
```

But this was a red herring. So I resorted to the good ol `strings grep` way.
```
strings memory | grep "KashiCTF"
KashiCTF{Fake_Flag}
KashiCTF{Fake_Flag}
KashiCTF{Fake_Flag}
KashiCTF{DF1R_g03555_Brrrr}
```

**Flag:** `KashiCTF{DF1R_g03555_Brrrr}`
