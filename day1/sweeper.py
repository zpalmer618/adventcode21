#!/usr/bin/python

# Open the input file and slurp it into memory
with open('depth.txt') as infile:
    stuff = infile.read()

# Split the list into individual values and take off annoying trailing
# character
lis = stuff.split("\n")
depth = lis[:-1]

# Convert list of strings to integers
for i in range(len(depth)):
    depth[i] = int(depth[i])

# Compare each entry pairwise to determine how often the depth
# increases
count = 0
prev = depth[0]
for num in depth:
    if num > prev:
        count += 1
    prev = num
print(count)

# Compare sets of three pairwise to determine how often the depth of
# sets of three increase
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
