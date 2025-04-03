import sys
king, stone, n = map(str, sys.stdin.readline().split())
move = [sys.stdin.readline().rstrip() for _ in range(int(n))]
dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
king_now = (dic[king[0]], int(king[1]))
stone_now = (dic[stone[0]], int(stone[1]))
for i in range(int(n)):
    mv = move[i]
    x, y = 0, 0
    if mv == 'R':
        x, y = 1, 0
    elif mv == 'L':
        x, y = -1, 0
    elif mv == 'B':
        x, y = 0, -1
    elif mv == 'T':
        x, y = 0, 1
    elif mv == 'RT':
        x, y = 1, 1
    elif mv == 'LT':
        x, y = -1, 1
    elif mv == 'RB':
        x, y = 1, -1
    elif mv == 'LB':
        x, y = -1, -1

    if 0 < king_now[0] + x < 9 and 0 < king_now[1] + y < 9:
        tmp = (king_now[0] + x, king_now[1] + y)
        if tmp == stone_now:
            if 0 < stone_now[0] + x < 9 and 0 < stone_now[1] + y < 9:
                stone_now = (stone_now[0] + x, stone_now[1] + y)
                king_now = (king_now[0] + x, king_now[1] + y)
        else:
            king_now = (king_now[0] + x, king_now[1] + y)

def find(target):
    for k, v in dic.items():
        if v == target[0]:
            print(k, end="")
            print(target[1])
            return

find(king_now)
find(stone_now)