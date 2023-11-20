import sys
s = sys.stdin.readline().rstrip()
q = int(sys.stdin.readline())

li = [[0]*26 for _ in range(len(s)+1)]

for i in range(1, len(s)+1):
    for j in range(26):
        if ord(s[i-1]) - 97 == j:
            li[i][j] = li[i-1][j] + 1
        else:
            li[i][j] = li[i-1][j]

for _ in range(q):
    a, b, c = sys.stdin.readline().split()
    a, b, c = ord(a)-97, int(b), int(c)
    print(li[c+1][a] - li[b][a])


