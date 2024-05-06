import sys
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
num = 0

for i, v in enumerate(li[::-1]):
    num += v*(a**i)

result = []
while num//b:
    result.append(num%b)
    num //= b
result.append(num)

print(*result[::-1])
# 16 * 1 = 16
# 2 * 17
# 3 *
# 17*2 = 34 + 16 = 50
# 50//8 6 50%8 2
