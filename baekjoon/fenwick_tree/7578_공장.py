import sys

def update(tree, idx, val):
    while idx < len(tree):
        tree[idx] += val
        idx += idx & -idx


def query(tree, idx):
    result = 0
    while idx > 0:
        result += tree[idx]
        idx -= idx & -idx
    return result

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a_map = {num: i for i, num in enumerate(a)}
mapped = [a_map[num] for num in b]

size = n+2
tree = [0] * size

inversion = 0
for i in mapped:
    inversion += query(tree, n) - query(tree, i+1)
    update(tree, i+1, 1)

print(inversion)

# 순열에서 역순쌍 문제와 동일

# qeury(n) - query(i+1)
# 지금까지 입력 중 i 보다 큰 값의 개수를 구하기 위해
# qeury(n) - query(i+1) -> 이는 i+1보다 큰 값들의 개수를 의미함

# 펜윅 트리 or BIT(Binary Indexed Tree)
# 구간 합 혹은 누적 합을 빠르게 갱신 및 쿼리할 수 있는 자료구조

# 사용처
# 1. 배열의 부분 합을 빠르게 구하고 싶을 때
# 2. 배열의 원소를 갱신할 일이 잦을 때
# 3. 예: 역순쌍 개수, K번째 수 구하기, 좌표 압축 후 구간 처리

# 시간복잡도 : O(log N)
# update(i, x) -> i번째 위치에 x를 더함
# query(i) -> 1부터 i까지의 합

# 구조
# 1-based 인덱스
# 내부적으로 인덱스의 최하위비트(LSB)를 사용해 범위를 관리함

# update(i, x): i번째에 값 x를 더하기
# def update(i, x):
#     while i < len(tree):
#         tree[i] += x
#         i += (i & -i)  # LSB만큼 증가

# query(i): 1부터 i까지의 누적합 구하기
# def query(i):
#     res = 0
#     while i > 0:
#         res += tree[i]
#         i -= (i & -i)  # LSB만큼 감소
#     return res

# i & -i는 i의 최하위 비트(가장 작은 2의 거듭제곱)를 추출하는 테크닉