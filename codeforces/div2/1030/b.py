import sys
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ops = []

    for i in range(1, n + 1):
        if i < n:
            ops.append((i, i + 1, n))
        ops.append((i, 1, i))

    print(len(ops))
    for op in ops:
        print(*op)

    # for i in range(2, n + 1):
    #     res.append((i, 1, n))
    #     if i == 2:
    #         continue
    #     for j in range(2, n):
    #         if 1 != j:
    #             res.append((i, 1, j))
    #         if j+1 != n:
    #             res.append((i, j+1, n))
    #
    # print(len(res))
    # for op in res:
    #     print(*op)

# 1 2 3
# 3 2 1 (2/1/3)
# 2 3 1 (3/1/3, 3/1/2)

# 1 2 3 4
# 4 3 2 1 (2/1/4)
# 3 4 1 2 (3/1/4, 3/1/2, 3/3/4)
# 2 1 4 3 (4/1/4, 4/1/3)

# 1 2 3 4
# 4 1 2 3 (2/1/4, 2/2/4)
# 3 4 1 2 (3/1/4, 3/1/2, 3/3/4)
# 2 3 4 1 (4/1/4, 4/1/3)

# 1 2 3 4
# 4 3 2 1
# 3 4 1 2
# 2 1 4 3

# 1 2 3
# 2 1 3
# 3 2 1

# 1 2 3 4
# 2 1 3 4
# 3 2 1 4
# 4 3 2 1