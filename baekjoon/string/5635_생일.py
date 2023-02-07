import sys
n = int(sys.stdin.readline())
li = []

for _ in range(n):
    li.append(list(sys.stdin.readline().rstrip().split()))

li.sort(key=lambda x : (int(x[3]), int(x[2]), int(x[1])))

print(li[len(li)-1][0])
print(li[0][0])


