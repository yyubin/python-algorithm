from collections import defaultdict
x_dic = defaultdict(int)
y_dic = defaultdict(int)
for _ in range(3):
    x, y = map(int, input().split())
    x_dic[x] += 1
    y_dic[y] += 1


li1 = sorted(x_dic.items(), key=lambda x: x[1])
li2 = sorted(y_dic.items(), key=lambda x: x[1])

print(li1[0][0], li2[0][0])
