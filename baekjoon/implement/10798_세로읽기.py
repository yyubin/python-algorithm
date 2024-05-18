import sys
len_ = 0
li = []
for _ in range(5):
    string = sys.stdin.readline().rstrip()
    len_ = max(len_, len(string))
    li.append(list(string))

for i in range(5):
    if len(li[i]) != len_:
        li[i] = li[i] + [''] * (len_ - len(li[i]))

li = list(zip(*li))
for i in li:
    print(*i, sep="", end="")





# Aa0aPAf985Bz1EhCz2W3D1gkD6x
# Aa0aPAf985Bz1EhCz2W3D1gkD6x