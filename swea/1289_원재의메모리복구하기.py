for tc in range(int(input())):
    li = list(map(int, input()))
    diff = 0
    ans = 0
    for i in li:
        if i != diff:
            ans += 1
            diff = i

    print('#'+str(tc+1), ans)


