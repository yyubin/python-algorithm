import sys
s = list(sys.stdin.readline().rstrip())
s_li = []

while len(s) > 0:
    s_li.append(''.join(s))
    s.pop(0)

s_li.sort()
print(*s_li, sep="\n")
