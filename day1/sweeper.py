#!/usr/bin/python

# Import input values into a list
with open('depth.txt') as infile:
    stuff = infile.read()

depth = stuff.split("\n")
meas = depth[:-1]

base = meas[0]
count = 0

# Check if every value in the list is greater than the previous value
for depth in meas:
    # if depth == base:
        # print(f"""{depth} [No previous measurement]""")
    # Had to use the int() becuase I was comparing the numbers as strings instead of their integer value
    if int(depth) > int(base):
        count += 1
        # print(f"""{depth} [increased]""")
    # else:
        # print(f"""{depth} [decreased]""")
    # print("BEEP\n")
    base = depth
# Print number of times the value increases
print(count)
