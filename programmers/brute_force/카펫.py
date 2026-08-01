def solution(brown, yellow):
    total = brown + yellow
    for i in range(1, yellow+1):
        if yellow%i != 0:
            continue
        row = yellow//i
        section = (row + 2) * (i + 2)

        if section == total:
            if i > row:
                return [i+2, row+2]
            else:
                return [row+2, i+2]

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))