#  Game 1 - Untitled Game

Domain: Rev

Points: 100

Solves: 237

### Given information

> We made a game.

### Solution

Writeup author: taci

We are given a game as the challenge file which upon opening puts us in a confined space with only one interactable object - a computer which prompts us for a password.

![image](https://github.com/user-attachments/assets/98184741-599a-4715-b013-0bf38ec39a35)

Tried to look for the password in the code of the game. We can view the code by running `strings` on the file. Now trying to look for the password I came across the flag itself.

```
strings Challgame.exe
```

![image](https://github.com/user-attachments/assets/a16df3d1-8eee-4a21-a136-a69ea80d2b8c)

**Flag:** `KashiCTF{N07_1N_7H3_G4M3}`
