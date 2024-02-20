
# Combinatorial Conundrum

Category: Misc
Solves: 17
### Given information:

>MogamBro has guarded your flag behind a grand equation. The equation involves 26 mysterious integers each constrained by a set of peculiar bounds. You need to find the number of solutions for the sum. The flag is equal to the remainder when the number of solutions is divided by 69696969.
  Wrap the flag that you get in BITSCTF{}

There's also a challenge file given, the content:


>MogamBro has guarded your flag behind a grand equation. The equation involves 26 mysterious integers each constrained by a set of peculiar bounds. You need to find the number of solutions for the sum:
>
>x1 + x2 + ... x26 = 69696969
>
>
>The bounds are:
>
>2008 <= x1  < 67434882
>5828 <= x2  < 35387831
>2933 <= x3  < 30133881
>411  <= x4  < 63609725
>4223 <= x5  < 18566959
>1614 <= x6  < 25526751
>5679 <= x7  < 44298843
>6349 <= x8  < 26793895
>117  <= x9  < 40292840
>2321 <= x10 < 42293336
>2281 <= x11 < 26301527
>1939 <= x12 < 50793633
>6273 <= x13 < 51546489
>1477 <= x14 < 36871159
>800  <= x15 < 65314188
>4727 <= x16 < 15882817
>2828 <= x17 < 40562779
>1782 <= x18 < 48186923
>1744 <= x19 < 37382713
>2486 <= x20 < 56149154
>6312 <= x21 < 18170199
>2188 <= x22 < 63940428
>5380 <= x23 < 58244044
>1772 <= x24 < 29193116
>2708 <= x25 < 22309445
>1528 <= x26 < 40848052
>
>
>The flag is equal to the remainder when the number of solutions is divided by 69696969.
>Wrap the flag that you get in BITSCTF{}

### Solution:

Here we have to find the number of non-negative integer solution to the equation `x1 + x2 + ... x26 = 69696969`  with the constraints on each variable given.

We can do that using combinatorics, There's a standard stars and bards method of counting to find the solution, [this](https://math.stackexchange.com/questions/203835/enumerating-number-of-solutions-to-an-equation) gives a nice explanation.
The main problem is that using the above method requires accounting for lots of cases where more than 2 variables be doubly,triply counted.

Inclusion-Exclusion principle provides for a much more efficient way to tackle the problem.[this](https://math.stackexchange.com/questions/34871/inclusion-exclusion-principle-number-of-integer-solutions-to-equations)  provides for a good explanation on how it works.

The script used:
```
# Correcting the usage of comb() function
from math import comb

# Define the target sum
target_sum = 69696969

# Define the bounds
bounds = [
    (2008, 67434882), (5828, 35387831), (2933, 30133881), (411, 63609725),
    (4223, 18566959), (1614, 25526751), (5679, 44298843), (6349, 26793895),
    (117, 40292840), (2321, 42293336), (2281, 26301527), (1939, 50793633),
    (6273, 51546489), (1477, 36871159), (800, 65314188), (4727, 15882817),
    (2828, 40562779), (1782, 48186923), (1744, 37382713), (2486, 56149154),
    (6312, 18170199), (2188, 63940428), (5380, 58244044), (1772, 29193116),
    (2708, 22309445), (1528, 40848052)
]

# Define the number of bounds
num_bounds = len(bounds)

# Define a function to calculate the sum of integers within bounds
def sum_within_bounds(k):
    total = 0
    for i in range(1 << num_bounds):
        sign = -1 if bin(i).count('1') % 2 == 0 else 1
        current_sum = 0
        for j in range(num_bounds):
            if (i >> j) & 1:
                current_sum += bounds[j][0]
            else:
                current_sum += bounds[j][1]
        # Check if the argument for comb() is non-negative
        if k - current_sum + num_bounds - 1 >= 0:
            total += sign * comb(k - current_sum + num_bounds - 1, num_bounds - 1)
    return total

# Apply inclusion-exclusion principle
result = abs(sum_within_bounds(target_sum)) # Taking absolute value to ensure non-negativity

print("Number of solutions:", result)
print("flag:BITSCTF{"+str(result)+"}")
```

The flag is : BITSCTF{10414036}







