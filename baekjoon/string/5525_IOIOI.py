import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
i = 0
cnt = 0
res = 0

while i < m-1:
    if s[i] == 'I' and s[i+1] == 'O':
        cnt = 0
        while i + 2 < m and s[i+1] == 'O' and s[i+2] == 'I':
            cnt += 1
            i += 2
            if cnt == n:
                res += 1
                cnt -= 1
        i += 1
    else:
        i += 1

print(res)
# O(N * M)
# import sys
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# s = sys.stdin.readline().rstrip()
# st = 'I' + ('OI' * n)
# cnt = 0
# for i in range(m - len(st)+1):
#     if s[i:i+len(st)] == st:
#         cnt += 1
# print(cnt)