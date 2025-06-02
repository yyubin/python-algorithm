import sys
n = int(sys.stdin.readline())
li = sys.stdin.readline().rstrip()

op = (n-1) // 2
picked = [False] * op
ans = -sys.maxsize

def cal():
    tmp = list(li)
    for j in reversed(range(op)):
        if picked[j]:
            tmp.insert(j*2, "(")
            tmp.insert(j*2+4, ")")
    return eval("".join(tmp))

def bt(idx):
    global ans
    if idx >= op:
        ans = max(ans, cal())
        return

    bt(idx+1)

    if idx == 0 or not picked[idx-1]:
        picked[idx] = True
        bt(idx+1)
        picked[idx] = False

bt(0)
print(ans)

# 비트마스킹 풀이
# import sys
# n = int(sys.stdin.readline()) // 2
# li = sys.stdin.readline().rstrip()
# res = -sys.maxsize
# for i in range(1 << n):
#     if i & (i<<1):
#         continue
#     tmp = [*li]
#     for j in reversed(range(n)):
#         if i & (1<<j):
#             tmp.insert(j*2+3, ")")
#             tmp.insert(j*2, "(")
#     res = max(res, eval("".join(tmp)))
# print(res)