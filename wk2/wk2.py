import re

hand = open('sample.txt')
x = 0

for line in hand:
    line = line.rstrip()
    y = re.findall('[0-9]+', line)
    if re.findall('[0-9]+', line) :
        y = list(map(int, y))
        x = x+sum(y)

print(x)
