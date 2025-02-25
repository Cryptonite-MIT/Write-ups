# Do Not Redeem #2
Domain: Forensics

Points: 434

Solves: 62

### Given information
> Kitler says he didn't request that OTP, neither did he read or share it. So it must be the scammer at play. Can you figure out the package name of the application that the suspected scammer used to infiltrate Kitler? Wrap your answer within `KashiCTF{` and `}`
> 
> Flag format: `KashiCTF{com.example.pacage.name}`
> 
> Download `kitler's-phone.tar.gz` : Use the same file as in the challenge description of [forensics/Do Not Redeem #1](https://kashictf.iitbhucybersec.in/challenges#Do%20Not%20Redeem%20#1-28)

### Solution
Writeup author: detectivepikachu

1. This is an extension of the previous Do Not Redeem challenge (#1), we now navigate the extracted file contents and look for the packages that might be used to infiltrate the target.
  
2. Since we are supposed to look for packages that seem suspicious, we navaigate to `/data/app/` from the root directory, where we find **directories for various application package names** for applications installed on Kitler's Android device.

3. We discovered that there are 9 apps installed, so our approach was to try package names of apps that might be used to gain access to a device, or which have *administrative access* over a device, however this approach didn't work out.

4. However after careful observation, we notice that there is a *second* app package name pretending to be a **calendar app**. This package is following a suspicious naming scheme, as it is named **`com.google.calendar.android`**, which is a change in naming convention from **`com.google.android.XXXX`**, which is usually how Google app packages are named. We can also find the original calendar app on the device in another folder `/data/data` called `com.google.android.calendar` (not being used for impersonation).

5. Wrapping the suspicious app package name in the flag format, gives us the flag.

**Flag: `KashiCTF{com.google.calendar.android}`**
