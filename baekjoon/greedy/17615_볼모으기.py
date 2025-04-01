import sys

n = int(sys.stdin.readline())
balls = list(sys.stdin.readline().rstrip())
r, b = balls.count('R'), balls.count('B')
def count_ball(x):
    global r, b
    tmp = 0
    left, right = 0, 0
    for i in balls:
        if i == x:
            left += 1
        else:
            break
    for i in balls[::-1]:
        if i == x:
            right += 1
        else:
            break

    d = max(left, right)
    if x == 'R':
        tmp = r - d
    else:
        tmp = b - d

    return tmp
res = min(count_ball('B'), count_ball('R'))
print(res)

# 시간복잡도 O(n)