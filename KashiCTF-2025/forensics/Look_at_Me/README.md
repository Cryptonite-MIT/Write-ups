# Look at Me

**Domain:** Forensics

**Points:** 300

**Solves:** 106

### **Given Information**

> There is something wrong with him.. What can it be??

### **Solution**

**Writeup author:** lvert

1. **Identifying the Tool Used for Steganography:**
   - Performing a **reverse image search** on the provided `.jpg` file reveals that it matches the icon of **SilentEye**, a well-known steganography tool.
   - This suggests that the image contains hidden data embedded using SilentEye’s encoding feature.

2. **Extracting the Hidden Data:**
   - Download and install **SilentEye** (available for Windows and Linux).
   - Open **SilentEye** and load the `.jpg` file into the program.
   - Click the **"Decode"** option to analyze the image for hidden messages.

3. **Retrieving the Flag:**
   - The decoding process extracts a hidden text message, revealing the flag.

**Flag:** `KashiCTF{K33p_1t_re4l}`

