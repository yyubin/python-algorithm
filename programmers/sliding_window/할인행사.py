from collections import defaultdict
def solution(want, number, discount):
    answer = 0
    dic = defaultdict(int)
    num_dic = dict(zip(want, number))

    for w in want:
        dic[w] = 0

    for i in range(10):
        dic[discount[i]] += 1

    for w in want:
        if dic[w] < num_dic[w]:
            break
    else:
        answer += 1

    for i in range(len(discount) - 10):
        dic[discount[i]] -= 1
        dic[discount[i+10]] += 1

        for w in want:
            if dic[w] < num_dic[w]:
                break
        else:
            answer += 1

    print(answer)
    return answer


solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])
solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"])