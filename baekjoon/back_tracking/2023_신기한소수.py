import sys
n = int(sys.stdin.readline())

def find(x):
    for i in range(2, int(x**0.5) + 1):
        if int(x) % i == 0:
            return False
    return True


def dfs(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(10):
            temp = num * 10 + i
            if find(temp):
                dfs(temp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)

#시도하다 검색해봄
#첫숫자는 전부 소수(2,3,5,7)
#for문으로 들어온 숫자에 10곱하고 하나씩(1~9) 더해보고
#소수가 맞으면 다음단계
