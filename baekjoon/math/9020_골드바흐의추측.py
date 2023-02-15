import sys
t = int(sys.stdin.readline())


def is_prime(num): #에라토스테네스의
    d = [False, False] + [True] * (num-1)
    for i in range(2, num+1):
        if d[i]:
            primes.append(i)
            for j in range(2*i, num+1, i):
                d[j] = False


for _ in range(t):
    n = int(sys.stdin.readline())
    primes = []
    result = []

    is_prime(n)
    for i in primes:
        for j in primes:
            if i + j == n:
                result.append((abs(i-j), i, j))
                break

    result.sort(key=lambda x: x[0])
    print(result[0][1], result[0][2])
