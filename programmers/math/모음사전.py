from itertools import product

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    li = []
    for i in range(1, 6):
        for c in product(vowels, repeat=i):
            li.append("".join(c))

    li.sort()
    return li.index(word) + 1

print(solution("AAAAE"))
print(solution("AAAE"))

## product 모든 조합