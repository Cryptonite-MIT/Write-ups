## Covert Communications Challenge Solution Overview

### Initial Analysis
Received a `.png` image and a `.wav` audio file. Initial examination of the `.wav` file's spectrogram revealed no secrets, but treating the audio as SSTV (Slow Scan Television) noise was suggested, leading to the discovery of another image.

### Decoding the SSTV Image
Using an SSTV decoding tool, I converted the audio file into an image that contained a ZIP archive named `secret.zip,` which was password-protected.

### Extracting the ZIP Archive
The password `mogambro` (found within the challenge context or possibly within the provided images) unlocked the ZIP archive, revealing two `.pkl` files: `enc_data.pkl` and `tempo.pkl`.

### Deciphering the Message
The challenge hinted at using Huffman coding and histogram analysis to decode the hidden message. So, it was deduced that the `.png` image contained the encrypted message using steganography, specifically histogram shifting and Huffman coding.

### Using External Resources
A GitHub repository ([TejveerSingh13/Image-Steganography](https://github.com/TejveerSingh13/Image-Steganography)) was found that matched the challenge's requirements. This repository demonstrated how to use Huffman coding and histogram shifting for steganography.

### Decoding the Final Message
The hidden message encoded in the image was successfully extracted from the GitHub repository.

The final flag was: `bitsctf{s73g4n06r4phy_15_n07_45_345y_45_17_533m5}`.
