# Stego Gambit

Domain: Forensics

Points: 480

Solves: 35

### Given information

> Do you dare to accept the Stego Gambit? I know you can find the checkmate but the flag!! 
> ![chall](https://github.com/user-attachments/assets/f06538cc-c43d-4afa-a577-355bd90ca016)


### Solution

Writeup author: Kafka

- Using strings on the image, you'd find "Use the moves as key to the flag, separated by \_"
-  Gambit is when the player has to make a sacrifice, and the description mentioned checkmate so using *lichess* analysis the best move sequence, where white is moving first, is: 
  Bh1 -> Kxa2 -> Qg2#

- A move is when both white and black complete their turns. So one move  would be `Bh1Kxa2` and the other `Qg2#`, and using the file format given it would be `Bh1Kxa2_Qg2#`
- This is the passphrase which would be useful to extract text files from the JPG using *steghide*, so the following:


```
$ steghide extract -sf chall.jpg -p Bh1Kxa2_Qg2#
```
- Steghide writes an extracted data to `flag.txt`. Which has the flag for the challenge. 
 

**Flag: `KashiCTF{573g0_g4m617_4cc3p73d}`**
