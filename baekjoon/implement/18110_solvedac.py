import sys
n = int(sys.stdin.readline())
if n == 0:
    print(0)
    sys.exit()

li = [int(sys.stdin.readline()) for _ in range(n)]
li.sort()
cut = int(n * 0.15 + 0.5)
trimmed = li[cut:n - cut]
print(int(sum(trimmed) / len(trimmed) + 0.5))

# 마지막 프린트에서 사사오입 안해서 4번 제출함
# 왜 이런걸 까먹을까
