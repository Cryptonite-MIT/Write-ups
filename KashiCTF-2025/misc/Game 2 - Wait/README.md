# Game 2 - Wait

Domain: Miscellaneous

Points: 195

Solves: 132

### Given information

> We made a game.

### Solution

Writeup author: taci

After loading the game we can see that there is a counter that starts from `172800` and the text `sec left to form the flag please wait`.

![image](https://github.com/user-attachments/assets/80eff525-1ff3-44b7-af24-6fed873fcbb9)

Hence we need to somehow make the time `0`. As the game is made on `Godot Engine`, we can use `GDRE Tools` to decompile the game.

Now after extracting with [`GDRE Tools`](https://github.com/GDRETools/gdsdecomp). We see a bunch of files. The file of interest for us is `project.godot`. 

![image](https://github.com/user-attachments/assets/8dce7a1f-b0e7-4760-a131-3cb54cb370c1)

Now we open `project.godot` using `Godot Engine` and we analyse the code.

![image](https://github.com/user-attachments/assets/2734baf6-0c9f-4759-8d85-91c1bb7bba18)

We reinitialize `time_left` to `1` in the `_process` function. 

```
func _process(delta):
    var curr_time = Time.get_datetime_dict_from_system()
    time_left = 1
    $Label.text = str(time_left)
    update()
```

Now running the game after saving we get our flag:

![image](https://github.com/user-attachments/assets/fb49dd1a-a1f5-4855-ac24-1c8d3952529e)

### Alternate Solution

The script also has positions, we can edit the loop inside the `update` function to just do `child_pos = pos[i]`.
```
func update():
    for i in range($pixels.get_child_count()):
        $pixels.get_child(i).global_position = pos[i]
```

Flag: `KashiCTF{Ch4kr4_Vyuh}`
