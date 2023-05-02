import sys
from collections import deque
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
cnt = dict()
c = ''

for _ in range(3):
    string = sys.stdin.readline().rstrip()
    string = string.replace(" ", "")
    c += string

q = deque()
c = c.replace("0", "9")
q.append(c)
cnt[c] = 0

while q:
    now = q.popleft()
    if '123456789' == now:
        print(cnt[now])
        break
    pos = now.find('9')
    x, y = pos // 3, pos % 3
    for k in range(4):
        ddx = x + dx[k]
        ddy = y + dy[k]
        if 0 <= ddx < 3 and 0 <= ddy < 3:
            npos = ddx * 3 + ddy
            next_num = list(now)
            next_num[npos], next_num[pos] = next_num[pos], next_num[npos]
            next_num = ''.join(next_num)

            if not cnt.get(next_num):
                q.append(next_num)
                cnt[next_num] = cnt[now] + 1
else:
    print(-1)






