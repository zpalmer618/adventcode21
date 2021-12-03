#!/usr/bin/python

# Read in the data and separate into individual lines
with open('test.dat') as infile:

# This is an example of list comprehension that says make a new list
# "[]" called lines that contains the output from the read lines
# "infile.readlines()" from the file that have been stripped of their
# new line characters "x.rstrip()."
    lines = [x.rstrip() for x in infile.readlines()]

# Initialize lists of zeros to add to to count the number of zeros and ones
ones = [0,0,0,0,0]
zeros = [0,0,0,0,0]
gamma = []

# Count if the first element of each line is either "0" or "1" and
# increment the respective list

for line in lines:
    for i in range(len(line)):
        if line[i] == "1":
            ones[i] += 1
        else:
            zeros[i] += 1

# Compare each element of the list to each other to determine if "0"
# or "1" is the most common and print it

for i in range(len(ones)):
    if ones[i] > zeros[i]:
        gamma.append(1)
    else:
        gamma.append(0)

print(ones)
print(zeros)
print(gamma)
