import sys
n, p = map(int, sys.stdin.readline().split())
res = 0
hold = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    if (a, b) not in hold:
        hold.append((a, b))
        res += 1

    tmp = []
    tmp_cnt = 0

    for mel, fret in hold:
        if mel == a and fret > b:
            tmp_cnt += 1
        else:
            tmp.append((mel, fret))

    hold = tmp
    res += tmp_cnt

print(res)



# 2 8
# 2 10
# 2 12
# 2 10
# 2 5

# add(2, 8)

# add(2, 10)

# add(2, 12)

# del(2, 12)

# del(2, 10)
# del(2, 8)
# add(2, 5)

# 1 5
# 2 3
# 2 5
# 2 7
# 2 4
# 1 5
# 1 3

# add(1, 5)

# add(2, 3)

# add(2, 5)

# add(2, 7)

# del(2, 7)
# del(2, 5)
# add(2, 4)

#

# del(1, 5)
# add(1, 3)
