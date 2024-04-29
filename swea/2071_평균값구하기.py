for tc in range(int(input())):
    li = list(map(int, input().split()))
    result = round(sum(li) / 10)
    print('#'+str(tc+1), result)
