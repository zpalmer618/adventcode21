#!/usr/bin/python

# Read in the input and separate each line
with open('inp.txt') as infile:
    lines = infile.read()

directions = lines.split("\n")
direcs = directions[:-1]

# Make each line a new list of key, value pairs
new_list = []
horiz = 0
depth = 0
aim = 0
for line in direcs:
    new_list = line.split()
    
# Given a key value pair, increase or decrease horiz, depth, and aim accordingly
    if new_list[0] == "forward":
        horiz += int(new_list[1])
        depth += int(new_list[1])*aim
    elif new_list[0] == "up":
        # depth -= int(new_list[1])
        aim -= int(new_list[1])
    elif new_list[0] == "down":
        # depth += int(new_list[1])
        aim += int(new_list[1])
print(horiz*depth)

