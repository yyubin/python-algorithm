import sys

num = int(sys.stdin.readline())
li = []
for i in range(abs(num)):
    if i%2 == 0:
        li.append(2**i)
    else:
        li.append(-2**i)
print(li)

li.reverse()
now = 0
ans = []





# 1 -2 4 -8 16 -32 ...
