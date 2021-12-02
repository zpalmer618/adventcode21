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
```
with open('depth.txt') as infile:
    stuff = infile.read()
```

Split the list into individual values and take off annoying trailing
character.
```
lis = stuff.split("\n")
depth = lis[:-1]
```

Convert list of strings to integers.
```
for i in range(len(depth)):
    depth[i] = int(depth[i])
```

Compare each entry pairwise to determine how often the depth
increases.
```
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
```
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


## Advent of Code: Day 1 - Learning to Pilot a Submarine

Now that you understand how the sonar sweeper works, you must figure
out how to pilot the submarine to avoid any untimely "meetings" with
your surroundings. The three commands the submarine takes are up X,
down X, and forward X, where "X" is a unit of measurement. In order to
pilot the craft effectively, you must determine your final horizontal
position and depth from a series of given commands.

From [Day 2](https://adventofcode.com/2021/day/2)
