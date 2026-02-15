def solution(prices):
    st = []
    n = len(prices)
    res = [0] * n

    for i in range(n):
        while st and prices[st[-1]] > prices[i]:
            idx = st.pop()
            res[idx] = i - idx

        st.append(i)

    while st:
        idx = st.pop()
        res[idx] = n - idx - 1

    return res


print(solution([1, 2, 3, 2, 3]))