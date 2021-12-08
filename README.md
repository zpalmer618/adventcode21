# Advent of Code 2021

A simple repository for my solutions to the [Advent of
Code](https://adventofcode.com/) projects. These will be attempted in
python, but I may branch out to other programming languages later to
work on those skills.

## Advent of Code: Day 1 - Sonar Sweeper

You are tasked with finding the keys to Santa's sleigh that were
dropped in the ocean. You are on an elf-made submarine and are tasked
with determining if every sweep on the sonar has either increased or
decreased in depth since the last sweep.

From: [Day 1](https://adventofcode.com/2021/day/1)

[My Solution](https://github.com/zpalmer618/adventcode21/blob/master/day1/sweeper.py):

Open the input file and slurp it into memory.
```python
with open('depth.txt') as infile:
    stuff = infile.read()
```

Split the list into individual values and take off annoying trailing
character.
```python
lis = stuff.split("\n")
depth = lis[:-1]
```

Convert list of strings to integers.
```python
for i in range(len(depth)):
    depth[i] = int(depth[i])
```

Compare each entry pairwise to determine how often the depth
increases.
```python
count = 0
prev = depth[0]
for num in depth:
    if num > prev:
        count += 1
    prev = num
print(count)
```

Compare sets of three pairwise to determine how often the depth of
sets of three increase.
```python
count = 0
i = 0
prev = sum(depth[i:i+3])
while i < len(depth)-2:
    val = sum(depth[i:i+3])
    if val > prev:
        count +=1
    prev = val
    i += 1
print(count)
```

## Advent of Code: Day 2 - Learning to Pilot a Submarine

Now that you understand how the sonar sweeper works, you must figure
out how to pilot the submarine to avoid any untimely "meetings" with
your surroundings. The three commands the submarine takes are up X,
down X, and forward X, where "X" is a unit of measurement. In order to
pilot the craft effectively, you must determine your final horizontal
position and depth from a series of given commands.

From [Day 2](https://adventofcode.com/2021/day/2)

[My Solution](https://github.com/zpalmer618/adventcode21/blob/master/day2/pilot.py):

Read in the input and separate each line
```python
with open('inp.txt') as infile:
    lines = infile.read()

directions = lines.split("\n")
direcs = directions[:-1]
```

Make each line a new list of key, value pairs
```python
new_list = []
horiz = 0
depth = 0
aim = 0
for line in direcs:
    new_list = line.split()
```
    
Given a key value pair, increase or decrease horiz, depth, and aim accordingly
```python
    if new_list[0] == "forward":
        horiz += int(new_list[1])
        depth += int(new_list[1])*aim
    elif new_list[0] == "up":
        aim -= int(new_list[1])
    elif new_list[0] == "down":
        aim += int(new_list[1])
print(horiz*depth)
```

## Advent of Code: Day 3 - Binary Diagnostic

The submarine started *Ms. Behavin'* so you decide to collect a
diagnostic report. In order to do so you must sift through a boatload,
or in your case a submarine-load, of binary data to determine the
power consumption and life support rating.

From [Day 3](https://adventofcode.com/2021/day/3)

[My Solution](https://github.com/zpalmer618/adventcode21/blob/master/day3/diagnostic.py)

Read in the data and separate into individual lines
```python
with open('val.txt') as infile:
```

This is an example of list comprehension that says make a new list
"[]" called lines that contains the output from the read lines
"infile.readlines()" from the file that have been stripped of their
new line characters "x.rstrip()."
```python
    lines = [x.rstrip() for x in infile.readlines()]
```

Initialize a list of zeros that is equal to the length of one row
```python
l = []

for i in range(len(lines[0])):
   l.append(0)
```

Count if the first element of each line is either "0" or "1" and
increment the respective list
```python
for line in lines:
    for i in range(len(line)):
        if line[i] == "1":
            l[i] += 1
        else:
            l[i] -= 1
```

Compare each element of the list to each other to determine if "0"
or "1" is the most common and print it
```python
g = []
e = []
for i in range(len(l)):
    if l[i] > 0:
        g.append(1)
        e.append(0)
    else:
        g.append(0)
        e.append(1)
```

Converts each element of the list into a string to use the join()
function (only operates on strings) that joins them with no
delimiter. This is then turned back into an integer in the int()
wrapper(?). Finally, the "2" is the second argument that turns
decimal into binary using int().
```python
gamma = int(''.join([str(i) for i in g]),2)
epsilon = int(''.join([str(i) for i in e]),2)

print("The power consumption rating is:", gamma*epsilon)
```

Defining functions that will be used to grab the column of numbers
from the list, the most and least common bit from said columns
```python
def column(i, lines):
    return [line[i] for line in lines]

def most_common(col):
    mc = 0
    num = 0
    for bit in col:
        if bit == "1":
            num += 1
        else:
            num -= 1
        if num >= 0:
            mc = 1
        else:
            mc = 0
    return mc

def least_common(col):
    lc = 0
    num = 0
    for bit in col:
        if bit == "1":
            num += 1
        else:
            num -= 1
    if num >= 0:
        lc = 0
    else:
        lc = 1
    return lc
```

Determines the most common bit from each column and trims the list
to contain the element of the list with the most common bits
```python
o2 = lines
for i in range(len(o2[0])):
    col = column(i, o2)
    b = most_common(col)
    o2 = [row for row in o2 if int(row[i]) == b]
```

Determines the least common bit from each column and trims the list
to contain the element of the list with the least common bits. There
is an additional "if" statement to overcome the problem that the last
bit of the last element of the list is always the most common and
would be deleted leaving an empty list
```python
co2 = lines
for i in range(len(co2[0])):
    if len(co2) < 2:
        break
    col = column(i, co2)
    b = least_common(col)
    co2 = [row for row in co2 if int(row[i]) == b]


o2 = int(''.join([str(i) for i in o2]),2)
co2 = int(''.join([str(i) for i in co2]),2)

print("The life support rating is: ", o2*co2)
```
