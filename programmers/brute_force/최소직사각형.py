def solution(sizes):
    cols = []
    rows = []

    for i in sizes:
        if i[0] > i[1]:
            cols.append(i[0])
            rows.append(i[1])
        else:
            cols.append(i[1])
            rows.append(i[0])

    return max(cols) * max(rows)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]] 	))