#!/usr/bin/python

test_list = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263
    ]
count = 0
prev = test_list[0]
for num in test_list:
    if num == prev:
        print(f"""{num} [No previous measurement]""")
    elif num > prev:
        count += 1
        print(f"""{num} [increased]""")
    else:
        print(f"""{num} [decreased]""")
    print("BEEP\n")
    prev = num
print(count)
