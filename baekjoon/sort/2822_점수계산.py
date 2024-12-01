import copy
import sys
score = [int(sys.stdin.readline()) for _ in range(8)]
top = copy.deepcopy(score)
top.sort(reverse=True)
top = top[:5]

li = []
for i in range(8):
    if score[i] in top:
        li.append(i+1)

li.sort()
print(sum(top))
print(*li)

