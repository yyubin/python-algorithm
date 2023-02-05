# 수리공 항승
# n, l = map(int, input().split())
# li = list(map(int, input().split()))
# li.sort()
#
# tape = 1
# start = li[0]
#
# for i in li[1:]:
#     if i in range(start, start + l):
#         continue
#     else:
#         start = i
#         tape += 1
#
# print(tape)

# 1205번 등수 구하기
n, score, p = map(int, input().split())
if n == 0:
    print(1)

else:
    li = list(map(int, input().split()))

    if len(li) + 1 > p and min(li) >= score:
        print(-1)

    else:
        li.append(score)
        li.sort(reverse=True)

        print(li.index(score) + 1)
