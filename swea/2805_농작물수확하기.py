for t in range(int(input())):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    left, right = n//2, n//2+1

    result = 0
    for i, v in enumerate(graph):
        result += sum(v[left:right])
        if i < n//2:
            left -= 1
            right += 1
        else:
            left += 1
            right -= 1

    print('#'+str(t+1), result)

