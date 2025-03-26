import sys

s, p = map(int, sys.stdin.readline().split())
string = list(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))
res = 0
current = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for i in range(p):
    current[string[i]] += 1

def is_valid():
    return (
            current['A'] >= check[0] and
            current['C'] >= check[1] and
            current['G'] >= check[2] and
            current['T'] >= check[3]
    )

if is_valid():
    res += 1

for i in range(p, s):
    out_char = string[i - p]
    in_char = string[i]
    current[out_char] -= 1
    current[in_char] += 1
    if is_valid():
        res += 1

print(res)

# 해시맵 연산 O(1)
# 시간복잡도 O(S)
