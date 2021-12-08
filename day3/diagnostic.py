#!/usr/bin/python

# Read in the data and separate into individual lines
with open('val.txt') as infile:

# This is an example of list comprehension that says make a new list
# "[]" called lines that contains the output from the read lines
# "infile.readlines()" from the file that have been stripped of their
# new line characters "x.rstrip()."
    lines = [x.rstrip() for x in infile.readlines()]

# Initialize a list of zeros that is equal to the length of one row
l = []

for i in range(len(lines[0])):
   l.append(0)

# Count if the first element of each line is either "0" or "1" and
# increment the respective list

for line in lines:
    for i in range(len(line)):
        if line[i] == "1":
            l[i] += 1
        else:
            l[i] -= 1

# Compare each element of the list to each other to determine if "0"
# or "1" is the most common and print it
g = []
e = []
for i in range(len(l)):
    if l[i] > 0:
        g.append(1)
        e.append(0)
    else:
        g.append(0)
        e.append(1)

# Converts each element of the list into a string to use the join()
# function (only operates on strings) that joins them with no
# delimiter. This is then turned back into an integer in the int()
# wrapper(?). Finally, the "2" is the second argument that turns
# decimal into binary using int().
gamma = int(''.join([str(i) for i in g]),2)
epsilon = int(''.join([str(i) for i in e]),2)

print("The power consumption rating is:", gamma*epsilon)

# Defining functions that will be used to grab the column of numbers
# from the list, the most and least common bit from said columns
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

# Determines the most common bit from each column and trims the list
# to contain the element of the list with the most common bits
o2 = lines
for i in range(len(o2[0])):
    col = column(i, o2)
    b = most_common(col)
    o2 = [row for row in o2 if int(row[i]) == b]

#Determines the least common bit from each column and trims the list
#to contain the element of the list with the least common bits. There
#is an additional "if" statement to overcome the problem that the last
#bit of the last element of the list is always the most common and
#would be deleted leaving an empty list
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
