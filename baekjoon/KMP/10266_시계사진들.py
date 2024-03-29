import sys

def pi(p):
    tmp = [0] * len(p)

    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = tmp[j-1]

        if p[i] == p[j]:
            j += 1
            tmp[i] = j
    return tmp

def kmp(s, p):
    table = pi(p)

    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j-1]

        if s[i] == p[j]:
            if j == len(p)-1:
                return True
            else:
                j += 1
    return False

n = int(sys.stdin.readline())

clock1 = [0] * 360000
clock2 = [0] * 360000

for a in map(int, sys.stdin.readline().split()):
    clock1[a] = 1

for b in map(int, sys.stdin.readline().split()):
    clock2[b] = 1

clock1 += clock1
print("possible" if kmp(clock1, clock2) else "impossible")