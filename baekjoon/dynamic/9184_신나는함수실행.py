import sys
d = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def initial():
    for a in range(21):
        for b in range(21):
            for c in range(21):
                if a <= 0 or b <= 0 or c <= 0:
                    d[a][b][c] = 1
                elif a < b < c:
                    d[a][b][c] = d[a][b][c-1] + d[a][b-1][c-1] - d[a][b-1][c]
                else:
                    d[a][b][c] = d[a-1][b][c] + d[a-1][b-1][c] + d[a-1][b][c-1] - d[a-1][b-1][c-1]

initial()

while True:
    aa, bb, cc = map(int, sys.stdin.readline().split())
    if aa == bb == cc == -1:
        break
    if aa <= 0 or bb <= 0 or cc <= 0:
        print(f'w({aa}, {bb}, {cc}) = 1')
        continue
    if aa > 20 or bb > 20 or cc > 20:
        print(f'w({aa}, {bb}, {cc}) = {d[20][20][20]}')
        continue

    print(f'w({aa}, {bb}, {cc}) = {d[aa][bb][cc]}')
