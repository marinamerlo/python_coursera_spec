numlist = list()
import re

hand = open('regex_sum_961653.txt')
for line in hand:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)', line)
    for i in stuff:
        num = int(i)
        numlist.append(num)
print(len(numlist))
print(sum(numlist))

