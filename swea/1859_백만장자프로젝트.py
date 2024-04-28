t = int(input())
for k in range(t):
    n = int(input())
    li = list(map(int, input().split()))

    result = 0
    trade = 0
    for i in li[::-1]:
        if trade < i:
            trade = i
        else:
            result += trade - i

    print('#'+str(k+1), result)
