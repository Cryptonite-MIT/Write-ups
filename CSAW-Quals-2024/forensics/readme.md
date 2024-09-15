
## ZipZipZip

In this challenge, we very quickly realise we need to recursive keep extracting the zip file.. and concatenate what appears to be a baes64 text.. Since there are about 13000 zip withnin one another (can be checked in central directory header with hex editor), we need to automate this process with some scripting.

Below script does exactly this...

```py
import zipfile
import os
import base64

def extract_nested_zip(zip_filename, base_name="chunk"):
    accumulated_text_file = f'{base_name}_accumulated.txt'
    current_zip = zip_filename
    
    with open(accumulated_text_file, 'w') as f:
        pass
    
    while True:
        with zipfile.ZipFile(current_zip, 'r') as zipf:
            text_filename = current_zip.replace('.zip', '.txt')
            with zipf.open(text_filename) as file:
                with open(accumulated_text_file, 'a') as acc_file:
                    acc_file.write(file.read().decode('utf-8'))
            
            files_in_zip = zipf.namelist()
            next_zip = [f for f in files_in_zip if f.endswith('.zip')]
            
            if not next_zip:
                break  # Exit loop if there are no more zip files
            
            current_zip = next_zip[0]            
            zipf.extract(current_zip)
        
        os.remove(zip_filename)
        zip_filename = current_zip

    with open(accumulated_text_file, 'r') as f:
        base64_string = f.read()
    
    image_data = base64.b64decode(base64_string)
    
    with open('output_image.jpg', 'wb') as image_file:
        image_file.write(image_data)
    
    os.remove(accumulated_text_file)
    if os.path.exists(current_zip):
        os.remove(current_zip)

extract_nested_zip('chunk_0.zip')
```
Zoom in bottom right and there's our flag.

![0](https://github.com/user-attachments/assets/45d1d6b7-ecb0-4b3e-8e63-c9f813feebe0)


#### Flag : ```csawctf{ez_r3cur5iv3ne55_right7?}```

***

## Covert

In this challenge, we are provided with a `chall.pcapng` and `keys.log`. Using the TLS keys within the latter, we can decrypt some of the traffic...      `(Edit > Preferences > TLS > Browse)`

We find an packet of value, `packet 79`... containing a python script that seems to be hiding data within lesser used IP header values...

```py
    # ez covert transfer...
    from scapy.all import IP, TCP, send

    key = ??

    dst_ip = "X.X.X.X"
    dst_port = ?????

    src_ip = "X.X.X.X"
    src_port = ?????

    def encode_message(message):
        for letter in message:
            ip = IP(dst=dst_ip, src=src_ip, id=ord(letter)*key)

            tcp = TCP(sport=src_port, dport=dst_port)

            send(ip/tcp)

    encode_message("????????????")
```
More info can be found in a [webpage](https://www.firstmonday.org/ojs/index.php/fm/article/download/528/449) referenced by later packets.

So the `Identification` value in IP headers is where the gold is at. `Packet 263 to 305` seem very suspicious because multiple retransmissions and their weird identitfication values.

![1](https://github.com/user-attachments/assets/9dfd3ba1-fa6d-4564-a1cb-7c201c0f533f)

The key can be easily figured out to be `55` knowing first letter of flag will be `c`. Decoding...

```py
ids = [5445, 6325, 5335, 6545, 5445, 6380, 5610, 6765, 5940, 5775, 5445, 5555, 6050, 1980, 5555, 5225, 6380, 2640, 5225, 6380, 6270, 3520, 6050, 6325, 5995, 5775, 6380, 5225, 5445, 2640, 6490, 5555, 6270, 6380, 4620, 3685, 4400, 1980, 1980, 1980, 6875]

key = 55
flag = ""

for id in ids:
    flag+=chr(int(id/key))

print(flag)
```

#### Flag : ```csawctf{licen$e_t0_tr@nsmit_c0vertTCP$$$}```

***

## The Three Illusions

Given are three images, use zsteg on all three of the images. 

hibuscus.png 

```
###########################
########## zsteg ##########
###########################

Watch out for red output. This tool shows lots of false positives...
imagedata           .. file: shared library
b1,rgb,lsb,xy       .. text: "ekasemk{oiiik_axiu_xsu_gieiwem_moi_nmivrxks_tmklec_ypxz}"
b2,r,lsb,xy         .. text: "\n*\n\n\n \n\" "
b2,r,msb,xy         .. text: "@PUUUUUUUUUUUUUUUUUU"
b2,g,msb,xy         .. text: "P@UUUUUUUUUUUUUUUUU"
b2,b,msb,xy         .. text: "@PATUUU@UU"
b2,rgb,msb,xy       .. text: "DUUPQUUU"
b2,bgr,msb,xy       .. text: ["U" repeated 10 times]
b2,rgba,lsb,xy      .. text: "?/;sgok/"
b2,abgr,msb,xy      .. text: "CCCGGWGCC"
b4,r,lsb,xy         .. text: "SU3\"#32\"3SV"
b4,r,msb,xy         .. text: "U5swSUUU5Ss"
b4,g,lsb,xy         .. text: "23\"\"TSTfuSD#33\"\"322&"
b4,g,msb,xy         .. text: "QUUaff&b&"
b4,b,lsb,xy         .. text: "dB\"\"\"$fh"
b4,b,msb,xy         .. text: "Qswwwwwww3swwwww3swwwwwwwwwwwwwwwwwwww32"
b4,rgb,lsb,xy       .. text: "Ct'Ce4RU#R$#eYF"
b4,rgb,msb,xy       .. text: "#uTGuRgq"
```

roses.png

```
###########################
########## zsteg ##########
###########################

Watch out for red output. This tool shows lots of false positives...
b1,rgb,lsb,xy       .. text: "csawctf{heres_akey_now_decrypt_the_vigenere_cipher_text} "
b1,bgr,lsb,xy       .. <wbStego size=5044673, data="\xB9Y\xD0\xFBh\xD1y\r\xC5\xDF"..., even=false, enc="wbStego 2.x/3.x", mix=true, controlbyte="\xD5">
b2,r,msb,xy         .. text: ["U" repeated 14 times]
b2,g,msb,xy         .. text: ["U" repeated 8 times]
b2,b,lsb,xy         .. text: "AQPPQTQQAQ@"
b2,b,msb,xy         .. text: ["U" repeated 22 times]
b2,rgba,lsb,xy      .. text: "7'cwggg#7'3w''cg"
b2,abgr,msb,xy      .. text: ["G" repeated 56 times]
b4,r,lsb,xy         .. text: ["\"" repeated 28 times]
b4,r,msb,xy         .. text: ["D" repeated 28 times]
```

datavsmetadata.png

```
###########################
########## zsteg ##########
###########################

Watch out for red output. This tool shows lots of false positives...
meta Comment        .. text: " Can you crack my secret? Here's a list of numbers: See what they reveal. 0 0 0 0 0 0 0 0 15 23 23 4 7 0 22 23 29 25 0 18 10 12 0 7 23 2 17 18 21 16 0 0 0 0 0 28 7 16 17 16 6 17 11 0 1 0 21 23 4 24 0 0 0 0 0 0"
b6,abgr,msb,xy      .. file: MPEG ADTS, layer III, v1, 192 kbps, Monaural
b7,abgr,lsb,xy      .. file: MPEG ADTS, layer I, v2, 256 kbps, Monaural
b8,abgr,lsb,xy      .. file: MPEG ADTS, layer II, v1, Monaural
b1,rgba,lsb,xy,prime.. text: ["w" repeated 52 times]
b1,abgr,msb,xy,prime.. text: ["w" repeated 52 times]
b2,r,lsb,xy,prime   .. file: VISX image file
b2,r,msb,xy,prime   .. file: 5View capture file
```

vignere the first ciphertext with the second as key 

`csawctf{heres_anew_key_decrypt_the_secretto_reveal_flag}`

xor both 

```
In [1]: first = b"csawctf{heres_anew_key_decrypt_the_secretto_reveal_flag}"

In [2]: second = [int(i) for i in "0 0 0 0 0 0 0 0 15 23 23 4 7 0 22 23 29 25 0 18 10 12 0 7 23 2 17 18 21 16 0 0 0 0 0 28 7 16 17 16 6 17 11 0 1 0 21 23 4 24 0 0 0 0 0 0".split(" ")]

In [3]: from Crypto.Util.strxor import strxor

In [4]: strxor(first, bytes(second))
Out[4]: b'csawctf{great_work_you_cracked_the_obscured_secret_flag}'
```


