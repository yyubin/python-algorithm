import sys
n = int(sys.stdin.readline())
people = {}

for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())

    if a not in people:
        people[a] = 0

    if b not in people:
        people[b] = 0

    if a == 'ChongChong':
        people[a] = 1

    if b == 'ChongChong':
        people[b] = 1

    if people[a] == 1 or people[b] == 1:
        people[a] = 1
        people[b] = 1

ans = 0
for i in people.items():
    if i[1] == 1:
        ans += 1
print(ans)




