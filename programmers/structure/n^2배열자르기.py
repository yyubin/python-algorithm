def solution(n, left, right):
    answer = []
    left_x, left_y = left//n, left%n
    right_x, right_y = right//n, right%n

    if left_x == right_x:
        for i in range(left_y, right_y + 1):
            answer.append(max(left_x, i) + 1)
        return answer

    for x in range(left_x, right_x+1):
        if x == left_x:
            for i in range(left_y, n):
                answer.append(max(x, i)+1)
        elif x == right_x:
            for i in range(right_y+1):
                answer.append(max(x, i)+1)
        else:
            for i in range(n):
                answer.append(max(x, i)+1)

    print(answer)
    return answer

solution(3, 2, 5)
solution(4, 7, 14)