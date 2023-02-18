import sys

array = [True for i in range(1000001)]

for i in range(2, 1001): #에라토스테네스의체 미리 구해두기(소수 전부 다구하면 시간초과)
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    for i in range(3, len(array)):
        if array[i] and array[n-i]:
            print(n, "=", i, "+", n-i)
            break
