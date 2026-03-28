import sys
li = []
for _ in range(int(sys.stdin.readline())):
    li.append(int(sys.stdin.readline()))

result = []
for i in range(min(li[0], li[-1])+1):
    tmp = [i]
    for j in range(len(li)-1):
        if li[j] - tmp[-1] < 0:
            break
        tmp.append(li[j] - tmp[-1])
    else:
        if tmp[0] + tmp[-1] == li[-1]:
            result = tmp
            break

print(*result, sep='\n')

