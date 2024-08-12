import sys
n = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
students = []

for _ in range(int(sys.stdin.readline())):
    students.append((map(int, sys.stdin.readline().split())))

def reverse(x):
    if x == 1:
        return 0
    else:
        return 1

for i, j in students:
    if i == 1:
        for k in range(j-1, n, j):
            switch[k] = reverse(switch[k])

    if i == 2:
        left, right = j-2, j
        cnt = 0
        while left >= 0 and right < n:
            if switch[left] == switch[right]:
                cnt += 1
                left -= 1
                right += 1
            else:
                break

        switch[j-1] = reverse(switch[j-1])
        for k in range(1, cnt+1):
            switch[j-1-k] = reverse(switch[j-1-k])
            switch[j-1+k] = reverse(switch[j-1+k])

switch.insert(0, 0)
for i in range(1, n+1):
    print(switch[i], end=" ")
    if i%20 == 0:
        print()
