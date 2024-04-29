for tc in range(int(input())):
    a, b = map(int, input().split())
    ans = '>'
    if a < b:
        ans = '<'
    elif a == b:
        ans = '='

    print('#'+str(tc+1), ans)
