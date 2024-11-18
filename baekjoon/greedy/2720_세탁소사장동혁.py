import sys
coins = [25, 10, 5, 1]
for _ in range(int(sys.stdin.readline())):
    c = int(sys.stdin.readline())
    for i in coins:
        print(c//i, end=" ")
        c %= i

