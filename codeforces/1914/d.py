import sys
def solution(first, second, third):
    s = set()
    s.add(first[0][0])
    tmp = first[0][1]

    for i in second:
        if i[0] not in s:
            s.add(i[0])
            tmp += i[1]
            break
    for i in third:
        if i[0] not in s:
            s.add(i[0])
            tmp += i[1]
            break
    return tmp

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))

    a = [(i+1, a[i]) for i in range(n)]
    b = [(i+1, b[i]) for i in range(n)]
    c = [(i+1, c[i]) for i in range(n)]
    a.sort(key=lambda x: -x[1])
    b.sort(key=lambda x: -x[1])
    c.sort(key=lambda x: -x[1])

    res = solution(a, b, c)
    res = max(res, solution(a, c, b))
    res = max(res, solution(b, c, a))
    res = max(res, solution(b, a, c))
    res = max(res, solution(c, a, b))
    res = max(res, solution(c, b, a))
    print(res)
    

