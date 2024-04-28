t = int(input())

for k in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    result = [0]
    tmp = [0]

    for i in range(n):
        for j, v in enumerate(result):
            tmp.append(result[j]+li[i])
        result = list(set(tmp))

    print('#'+str(k+1), len(result))
