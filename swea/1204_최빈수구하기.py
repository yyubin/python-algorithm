t = int(input())
for _ in range(t):
    tc = int(input())
    score = list(map(int, input().split()))
    dic = [0 for _ in range(101)]

    for i in score:
        dic[i] += 1

    max_idx = list(filter(lambda x: dic[x] == max(dic), range(len(dic))))
    print('#'+str(tc), max_idx[-1])
