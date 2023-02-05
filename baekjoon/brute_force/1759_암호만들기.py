from itertools import combinations

n, m = map(int, input().split())
li = list(combinations(list(input().split()), n))
li2 = []

vowel = [97, 101, 105, 111, 117]

for i in li:
    temp = []
    cnt = 0
    for j in i:
        temp.append(ord(j))
        if ord(j) in vowel:
            cnt += 1

    temp.sort()
    if temp not in li2 and 0 < cnt <= n-2:
        li2.append(temp)

li2.sort()
for i in li2:
    for j in range(len(i)):
        print(chr(i[j]), end="")
    print()
