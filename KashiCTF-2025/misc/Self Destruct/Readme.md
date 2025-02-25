# Self Destruct

Domain: misc

Points: 347

Solves: 94

### Given information

Explore the virtual machine and you might just find the flag. Or a surprise. Maybe....

NOTE: The attachment is a VirtualBox image. Do not run it outside VirtualBox. It is recommended to backup the .vdi file before launching the VM.

VM Parameters: (VirtualBox)
Type: Linux
Version: Debian (32 bits)
RAM: 1024MB
Storage: attached .vdi file

Username: kashictf
Password: kashictf

### Solution

Writeup author: Wixter_07

Mount as followed 

```
sudo modprobe nbd
sudo qemu-nbd --connect=/dev/nbd0 /path/to/disk.vdi
sudo fdisk -l /dev/nbd0
sudo mkdir /mnt/vdi
sudo mount /dev/nbd0p1 /mnt/vdi
```

Once you go into `/mnt/vdi/home/kashictf`, you can find a part of the flag from `.bash_history`

```bash
root:/mnt/vdi/home/kashictf# cat .bash_history
ls
echo "fLaG Part 5: 'ht??_No_Er'"
exit
```

Seems all flag parts are prepended as `fLaG Part <No.>` so we grep for the unique word `fLaG`.

```bash
root:/mnt/vdi/home/kashictf# grep -r "fLaG" /mnt/vdi 2>/dev/null
/mnt/vdi/etc/sudo.conf:# fLaG Part 6: 'r0rs_4ll0w'
/mnt/vdi/etc/hosts.allow:# fLaG Part 1: 'KashiCTF{r'
/mnt/vdi/etc/kernel-img.conf:# Kernel image management overrides fLaG Part 4: 't_Am_1_Rig'
/mnt/vdi/home/kashictf/.bash_history:echo "fLaG Part 5: 'ht??_No_Er'"
/mnt/vdi/home/kashictf/.sush_history:echo "fLaG Part 3: 'eserve_roo'"
```

I also tried this

```bash
root@:/mnt/vdi# find . -type f -exec grep "fLaG" {} \;
# fLaG Part 6: 'r0rs_4ll0w'
# fLaG Part 1: 'KashiCTF{r'
# Kernel image management overrides fLaG Part 4: 't_Am_1_Rig'
grep: ./usr/bin/sush: binary file matches
echo "fLaG Part 5: 'ht??_No_Er'"
echo "fLaG Part 3: 'eserve_roo'"
```

We see some matches in `/usr/bin/sush`. So we grep there

```bash
root:/mnt/vdi# strings /mnt/vdi/bin/sush | grep -i "fLaG"
fLaG Part 7: 'ed_Th0}'
fLaG Part 2: 'm_rf_no_pr'
```

The flag - **`KashiCTF{rm_rf_no_preserve_root_Am_1_Right??_No_Err0rs_4ll0wed_Th0}`**
