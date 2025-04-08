# import sys
# n, m = map(int, sys.stdin.readline().split())
# li = list(map(int, sys.stdin.readline().split()))
# li.sort(reverse=True)
# s = set()
#
# def back_tracking(cnt, tmp):
#     if cnt == m:
#         s.add(tmp)
#         return
#
#     for i in li:
#         for j in tmp:
#             if j > i:
#                 return
#         now = [i for i in tmp]
#         now.append(i)
#         back_tracking(cnt+1, tuple(now))
#
# back_tracking(0, ())
# res = list(s)
# res.sort()
# for i in res:
#     print(*i)

# 최악의 경우 O(N^M), 백트래킹이라 가지치기 하긴해서 탐색 속도는 이거보단 빠름


s = set()

def backtracking(start, seq):
    if len(seq) == m:
        if tuple(seq) not in s:
            print(*seq)
            s.add(tuple(seq))
        return
    for i in range(n):
        if seq and seq[-1] > numbers[i]:
            continue
        backtracking(i, seq + [numbers[i]])

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
backtracking(0, [])
# 조금더 개선
# 아니면 걍 조합으로 풀어도 되긴할듯
