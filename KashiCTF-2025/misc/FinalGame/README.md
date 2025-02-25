# FinalGame?

Domain: Misc

Points: 432

Solves: 63

### Given information

> We searched his room and found chess pieces thrown here and there ..thankfully someone recorded the entire game

https://lichess.org/incUSy5k

### Solution

Writeup author: Kafka


- Opening the *lichess* link given.
 ![image](https://github.com/user-attachments/assets/58413918-f0f5-43d7-8e03-169cb976f739)

-  On the left panel we could see all the games played in the game . Under the *Share and Export* tab Download *PGN*
- *PGN*  is a plain-text format for recording chess games . The *PGN* for this game is : 

```
1. b4 g6 2. e3 d5 3. Ne2 b5 4. Rg1 Bb7 5. c3 Qd7 6. Qb3 h6 7. Qd1 Qg4 8. Nf4 Nf6 9. Nh5 Qe4 10. Ng3 Qe5 11. Qf3 Bg7 12. Qh5 Ng4 13. c4 Qd6 14. cxb5 e6 15. Bb2 c6 16. Qxh6 Qd8 17. Bf6 Bxh6 18. Ne4 a6 19. Nec3 Bxe3 20. fxe3 Nf2 21. Rh1 Ne4 22. a4 Rh7 23. bxc6 Nf2 24. Bb5 Nxh1 25. Bh4 g5 26. Be2 Qc7 27. Bd3 Qa5 28. Bc4 Ra7 29. Na2 Qxa4 30. Nbc3 Nf2 31. Nd1 Rh6 32. Nc1 Qxc6 33. Ba2 Ng4 34. d4 Qc3+ 35. Kf1 Rf6+ 36. Kg1 Qc7 

```


- Since we have all the moves for the chess game , it could be some kind of move based stegnography or cipher. Looking up Chess Stegnography and ending up with this website -[this website](https://incoherency.co.uk/chess-steg/)

- Put the *PGN* in here to Unsteg it and get the flag : 

![image](https://github.com/user-attachments/assets/b642f81a-f99d-4688-a3ce-3ec203b9b36b)


**Flag: `KashiCTF{Will_This_Be_My_Last_Game_e94fab41}`**
