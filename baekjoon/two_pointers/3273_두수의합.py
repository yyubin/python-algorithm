n = int(input())
li = list(map(int, input().split()))
x = int(input())
result = 0

li.sort()

a, b = 0, n-1
while a < b:
    cal = li[a] + li[b]
    if cal == x:
        result += 1
        a += 1
        b -= 1
    elif cal > x:
        b -= 1
    else:
        a += 1

print(result)


