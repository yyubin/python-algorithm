import sys
from collections import Counter
n, m = map(int, sys.stdin.readline().split())
li = [sys.stdin.readline().rstrip() for _ in range(n)]
li = [i for i in li if len(i) >= m]
counter = Counter(li)
li = list(set(li))
li.sort(key=lambda x: (-counter[x], -len(x), x))
print(*li, sep="\n")

# sort 안에 li.count() 활용하게 되면 시간복잡도 O(n^2)까지 오를 수 있음
# 따로 counter를 사용하는게 나음

# Counter(li) -> O(n)
# set(li) -> O(n)
# sort() -> O(n log n)
# key는 O(1)
# 최종 시간복잡도 : O(n log n)