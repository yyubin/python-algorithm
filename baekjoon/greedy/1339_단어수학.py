import sys
from collections import defaultdict

n = int(sys.stdin.readline())
words = []
tmp = defaultdict(int)

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    words.append(word)
    # 자릿수에 대한 가중치는 10의 제곱으로 구현하는게 맞는듯..
    for i in range(len(word) - 1, -1, -1):
        tmp[word[i]] += 10 ** (len(word) - i)

sorted_tmp = sorted(tmp.items(), key=lambda x: -x[1])

num = 9
result = {}
for i in sorted_tmp:
    result[i[0]] = num
    num -= 1

ans = 0
for i in words:
    words_ = []
    for j in i:
        words_.append(result[j])
    ans += int(''.join(map(str, words_)))

print(ans)


