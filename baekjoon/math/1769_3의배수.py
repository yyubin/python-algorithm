import sys
n = [int(x) for x in sys.stdin.readline().rstrip()]
cnt = 0

while len(n) > 1:
    n = [int(x) for x in list(map(str, str(sum(n))))]
    cnt += 1

print(cnt)
print('YES' if n[0] in [3, 6, 9] else 'NO')

