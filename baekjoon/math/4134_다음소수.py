import sys
import math

def find_next_prime(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x%i == 0:
            return False
    return True

n = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(n)]

for i in li:
    if i == 0 or i == 1:
        print(2)
        continue

    while not find_next_prime(i):
        i += 1
    print(i)
