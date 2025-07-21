import sys
n, k = map(int, sys.stdin.readline().split())
li = [0] + list(map(int, sys.stdin.readline().split()))
li.sort()
left = 0
right = n
cnt = 0
res = 0

while cnt < k:
    if cnt % 2:
        left += 1
        cnt += 1
    else:
        res += li[right] - li[left]
        right -= 1
        cnt += 1
print(res)

# 가짜 값 0을 맨 앞에 삽입
# 첫 잔의 점수 = 그 잔의 맛
# 0을 ‘직전에 마신 맛’으로 만들어 두면
# 첫잔에서 맛–0 = 맛 이 바로 누적됨

# 이후 투포인터로 항상 가장 작은 남은 값 과 가장 큰 남은 값 을 O(1)에 얻게함

# left는 다음 valley(저점), right는 다음 peak(고점) 를 가리킴

# cnt의 짝 / 홀 로 ‘고점‑저점‑고점…’ 순서를 강제
# “올라갈 때만 점수” 조건에 맞게 점수를 더하고, 쓴 잔은 포인터를 이동해 버림

# https://feelingxd.tistory.com/68
