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
