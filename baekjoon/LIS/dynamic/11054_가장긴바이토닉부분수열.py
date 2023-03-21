import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
re_a = a[::-1]

increase = [1 for _ in range(n)]
decrease = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if re_a[i] > re_a[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for _ in range(n)]
for i in range(n):
    result[i] = increase[i] + decrease[n-i-1] - 1

print(max(result))

#증가하는 부분 감소하는 부분 각각 나눠서 가장 긴 부분 계산,
#증가부 감소부 합이 가장 큰 값이 정답