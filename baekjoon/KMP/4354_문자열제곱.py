import sys


def kmp(pattern):
    table = [0] * len(pattern)
    i = 0

    for j in range(1, len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i - 1]
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i

    return table


while True:
    string = sys.stdin.readline().rstrip()
    if string == ".":
        sys.exit()
    tmp = kmp(string)

    if len(string) % (len(string) - tmp[-1]) != 0:
        print(1)
    else:
        print(len(string)//(len(string) - tmp[-1]))

# failure function에서 문자열의 길이가 홀수인경우
# abababa에서 마지막 실패함수의 값은 5인데
# 이 문자열의 경우 a가 가장 짧은 문자열인 ab와 다르기때문에 답이 1나와야함
# 문자열 길이 홀수인부분에서 나눈 나머지가 0이면 1을 출력


