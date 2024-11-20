import sys
n, m = map(int, sys.stdin.readline().split())
li = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

dna = ['A', 'C', 'G', 'T']
ans = ''
cnt = 0
for i in range(m):
    tmp = [0, 0, 0, 0]
    for j in li:
        tmp[dna.index(j[i])] += 1
    idx = tmp.index(max(tmp))
    ans += dna[idx]
    cnt += sum(tmp) - max(tmp)

print(ans)
print(cnt)

## 순서 반드시 ['A', 'C', 'G', 'T']
## 이렇게 해서 오름차순으로 정렬하도록
