import sys
li = [i+1 for i in range(30)]

for _ in range(28):
    li.remove(int(sys.stdin.readline()))

li.sort()
print(li[0], li[1], sep="\n")