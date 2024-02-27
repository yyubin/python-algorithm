import sys
n = int(sys.stdin.readline())

for i in range(n):
    li = [int(c) for c in str(i)]
    li_sum = sum(li)
    if i + li_sum == n:
        print(i)
        sys.exit()

print(0)
