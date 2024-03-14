import sys
n = int(sys.stdin.readline())
li = [sys.stdin.readline().rstrip() for _ in range(n)]

def num(string):
    res = 0
    for i in string:
        if i.isdigit():
            res += int(i)
    return res

li.sort(key=lambda x: (len(x), num(x), x))
print(*li, sep="\n")
