import re

x = '3036 many reasons, ranging from making your living to solving 7209'

y = re.findall('[0-9]+', x)

y = list(map(int, y))

print(sum(y))
