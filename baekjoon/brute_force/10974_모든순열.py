import itertools

num = int(input())
li = [i+1 for i in range(num)]
nPr = list(itertools.permutations(li, num))

for i in range(len(nPr)):
    temp = list(nPr[i])
    print(*temp, sep=" ")