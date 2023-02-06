import sys
from collections import Counter
cnt = int(sys.stdin.readline())
li = []

for _ in range(cnt):
    li.append(int(sys.stdin.readline()))

li.sort()
li2 = Counter(li)
li2 = li2.most_common()


print(round(sum(li)/len(li)))         #산술평균
print(li[len(li)//2])                 #중앙값

if len(li) == 1:
    print(li2[0][0])
else:
    if li2[0][1] == li2[1][1]:        #최빈값
        print(li2[1][0])
    else:
        print(li2[0][0])
print(li[len(li)-1] - li[0])          #범위
