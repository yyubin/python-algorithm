for tc in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    print('#'+str(tc+1), *li)

