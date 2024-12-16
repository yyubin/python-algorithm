import sys

def ck(i, j, oper):
    if oper == '<':
        if i > j:
            return False
    if oper == '>':
        if j > i:
            return False

    return True

def bt(cnt, n):
    if cnt == k+1:
        ans.append(n)
        return

    for i in range(10):
        if not visited[i]:
            if cnt == 0 or ck(n[cnt-1], str(i), op[cnt-1]):
                visited[i] = True
                bt(cnt+1, n+str(i))
                visited[i] = False

k = int(sys.stdin.readline())
op = list(map(str, sys.stdin.readline().rstrip().split()))
visited = [False] * 10
ans = []
ans.sort()
bt(0, '')

print(ans[-1])
print(ans[0])




