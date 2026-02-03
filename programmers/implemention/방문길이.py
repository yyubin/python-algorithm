def solution(dirs):
    dic = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    now_x, now_y = 0, 0
    s = set()

    for d in dirs:
        tmp_x, tmp_y = now_x, now_y
        x, y = dic[d]
        if -5 <= tmp_x + x <= 5:
            tmp_x += x
        if -5 <= tmp_y + y <= 5:
            tmp_y += y
        if tmp_x == now_x and tmp_y == now_y:
            continue
        s.add((tmp_x, tmp_y, now_x, now_y))
        s.add((now_x, now_y, tmp_x, tmp_y))
        now_x, now_y = tmp_x, tmp_y

    return len(s)//2

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))