
def solution(citations):
    answer = 0
    citations.sort()
    left = 0
    right = max(citations) + 1

    while left <= right:
        mid = (left + right) // 2
        tmp_cnt = 0
        for i in citations:
            if mid <= i:
                tmp_cnt += 1

        if tmp_cnt >= mid:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)
    return answer

solution([3, 0, 6, 1, 5])