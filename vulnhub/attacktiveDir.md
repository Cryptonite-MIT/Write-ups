# TryHackMe Box Attacktive Directory(AD) \(Medium\)

## Enumeration

Running a nmap scan we find a lot of open ports, the ports of concern here are 139/445.
We enumerate the users using enum4linux because it's on port 139/445.

That doesn't work so well. So we can use a tool kerbute to enumerate users in which we find svc-admin and backup

`./kerbute userenum -d spookysec.local -dc spookysec.local -t 5 userlist.txt`

userlist given by tryhackme for reducded execution time.

## ASREPRoasting

Now that we have discovered a several usernames we can use a technique called ASREPRoasting, meaning if a user does not have the Kerberos preauthentication property selected it is possible to retrieve the password hash from that user.

We use /opt/impacket and getNPusers.py script to find the kerberos vuln user.
`python3 GetNPUsers.py spookysec.local/svc-admin -no-pass`

We get an hash for admin that we might be able to crack. And we get a hit with johnTheRipper.

___svc-admin: management2005___

## SMB Enumeration

Now that we have the admin, we can find out his shares with the domain controller and we find that admin does share backup.

`smbclient -L spookysec.local -U svc-admin`

We enumerate through all the shares but only find the content relevant in this share.
Enumerating the shares, one had some credentials inside :

`smbclient -L spookysec.local/backup -U svc-admin`

We get the backup_creds file onto our local machine using a `get command`.

The contents of that file looks like base64, decoding it we get the password to backup user.

___backup: backup2517860___

Now that we have the backup share we can dump all the past creds using impacket's __secretdump.py__

## Priv-esc

Now that we are in possession of the Administrator password hash. The next step will be performing a ___Pass the Hash Attack___.

Using a tool _evil-winrm_ we can do this.

`evil-winrm -i spookysec.local -u Administrator -H nt_hash_from_the_secrets_dump`

We got a windows shell now.

Flags for each user account can be located on each user's desktop.