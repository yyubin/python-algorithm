n = int(input())
li = [str(i+1) for i in range(n)]

for i in range(n):
    if '3' in li[i] or '6' in li[i] or '9' in li[i]:
        cnt = li[i].count('3') + li[i].count('6') + li[i].count('9')
        li[i] = '-' * cnt

print(*li)
