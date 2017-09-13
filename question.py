
# todo: Understand

import sys

a = sys.argv[0]
b = []

k = "abcde"
l = "12345"


z = {}
x = 0
while x < len(l):
    z[k[x]] = l[x]
    x += 1


for x in a:
    try:
        b.append(z[x])
    except KeyError:
        b.append(x)


print(''.join(b))

# fixme: Make it shorter
