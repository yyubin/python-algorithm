import sys
n = int(sys.stdin.readline())
levels = [int(sys.stdin.readline()) for _ in range(n)]
st = []
res = [0] * n

for i in range(n):
    level = levels[i]

    while st and st[-1][0] >= level:
        st.pop()

    if level == 1:
        st.append((level, i))

    else:
        if not st or st[-1][0] != level-1:
            print(-1)
            sys.exit()

        p = st[-1][1]
        res[p] += 1
        st.append((level, i))

print(*res, sep='\n')