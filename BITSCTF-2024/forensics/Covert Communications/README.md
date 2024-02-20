### CHALLENGE:
rskbansal hacked into nasa mainframe and intercepted a radio signal from deep space along with a very SUS image. 
He tried using data representation but soon realised that he seems to be missing something...Help him figure out the secret!!!
HINT: skbansal asked Huffman for help, he suggested to maybe try messing around with histograms.

### SOLVE:
The challenge description mentions 'deep space' which hints at using DeepSound for analyzing the wav file. </br>
On putting the secret.wav in DeepSound, we get a secret.zip file</br></br> 
![image](https://github.com/poorvi1910/Cryptonite/assets/146640913/87e55eca-613e-419f-91f2-03892ca8effa)

The zip file required a password to unzip.</br>
On using sstv on the wav file, we obtain the password of the zip file as 'mogambro' </br></br>
On entering the password, the zip file gave two pkl files: enc_data.pkl and temp.pkl </br>
The hint mentioned Huffman and histograms. Searching steganography techniques using Huffman and histograms I came across the below GitHub repo: </br>

https://github.com/TejveerSingh13/Image-Steganography </br>

The link contains a README file which has a youtube link along with written instructions as to how to use the attached python files that contain the actual working code for the Huffman Encoding and Compression algorithm. </br>

On using the enc_data.pkl file along with the decode option in the histo-shift.py code, we get a text file with a bunch of binary numbers. Now this text file and the tempo.pkl file need to be used in the huffman.py code which gives another text file that contains the decoded flag.

**FLAG: bitsctf{s73g4n06r4phy_15_n07_45_345y_45_17_533m5}**
