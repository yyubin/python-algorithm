for tc in range(int(input())):
    li = list(map(int, input().split()))

    result = 0
    for i in li:
        if i%2 == 1:
            result += i

    print('#'+str(tc+1), result)
