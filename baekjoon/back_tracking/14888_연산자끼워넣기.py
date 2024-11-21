import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
oper = list(map(int, sys.stdin.readline().split()))
max_, min_ = -sys.maxsize, sys.maxsize

def bt(i, ans, add, sub, mul, div):
    global max_, min_
    if i >= n:
        max_ = max(max_, ans)
        min_ = min(min_, ans)
        return
    if add > 0:
        bt(i+1, ans+li[i], add-1, sub, mul, div)
    if sub > 0:
        bt(i+1, ans-li[i], add, sub-1, mul, div)
    if mul > 0:
        bt(i+1, ans*li[i], add, sub, mul-1, div)
    if div > 0:
        bt(i+1, ans//li[i] if ans > 0 else -((-ans)//li[i]), add, sub, mul, div-1)


bt(1, li[0], oper[0], oper[1], oper[2], oper[3])
print(max_)
print(min_)
