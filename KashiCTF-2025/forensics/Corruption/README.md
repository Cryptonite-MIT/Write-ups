# Corruption
Domain: Forensics

Points: 100

Solves: 178


### Given information
> A corrupt drive I see...
> 
> Attachments: [image.iso](https://drive.google.com/file/d/1gHY5DOmUcZvfrLr-EpQWJfR3oiVCsYtD/view?usp=sharing)


### Solution
Writeup author: detectivepikachu

1. In the challenge we have been given a `image.iso` file, which is a bootable drive, so we try to run it by mounting it on a Virtual Machine software, like Oracle VirtualBox. However the file is corrupt and does not boot up. 
2. As a standard practice, we run the `$ file image.iso` commmand to try to understand more about it. This tells us that it is a `DOS/MBR boot sector`. 
3. Also try to extract the file contents of the given corrupt `image.iso` but that doesn't turn out to be helpful in getting to the flag.
4. Trying to use other methods to extract data, **we run the command `$ strings image.iso` to try to search for data stored in plaintext** in the file that might be of relevance. This helps us obtain the flag itself.

**Flag: `KashiCTF{FSCK_mE_B1T_by_b1t_Byt3_by_byT3}`**
