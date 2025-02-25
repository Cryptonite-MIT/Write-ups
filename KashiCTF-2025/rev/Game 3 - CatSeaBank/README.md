# Game 3 - CatSeaBank

Domain: Rev

Points: 479

Solves: 36

### Given information

> We made a game.

### Solution

Writeup Author: taci

We are given a game made with `Unity`. So we open `Assembly-Csharp.dll` using [`dnSpy`](https://github.com/dnSpy/dnSpy) as `Assembly-Csharp.dll` file usually contains all the game scripts in it.

![image](https://github.com/user-attachments/assets/169ac761-0c9c-4015-9e17-10111ccb4b39)

In the game we are asked to provide `2000` to a NPC but we only have `1000` in our bank, so we need to change this in the script. In `Start` method adding `this.currentBalance = 5000` will change our current balance to `5000` and we can give `2000` to the NPC.

![image](https://github.com/user-attachments/assets/e889d4e8-2015-4343-b45e-9044c57dd7aa)

After providing `2000` to the NPC, we get a `success` message and a certain `wisdom` wherein he says that `the secret is not in the open` and to `extract the archives`.

![image](https://github.com/user-attachments/assets/cc98ea53-5828-4e13-a5b7-a770e9c341ca)

So now we use [`Asset Ripper`](https://github.com/AssetRipper/AssetRipper) to extract all the assets of the game. Going through them we see a `flagfile` in `sharedassets0.assets` which was an audio file.

![image](https://github.com/user-attachments/assets/98e86585-caec-4fda-9de4-6ad917262a56)

![image](https://github.com/user-attachments/assets/35fcf599-dfb5-45fe-92ec-686263661d04)

So now export the file and open it using `Sonic Visualizer`. Additionally add a Spectrogram Layer. And we get our flag.

![image](https://github.com/user-attachments/assets/bb0b86a2-6a5a-49ff-b900-afe279225602)

**Flag:** `KashiCTF{1t_Wa5_Ju5t_4_Tutori4l_RIP}`
