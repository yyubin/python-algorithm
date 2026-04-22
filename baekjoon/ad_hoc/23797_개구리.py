import sys
st = list(sys.stdin.readline().rstrip())

k, p = 0, 0

for s in st:
    if s == 'K':
        if k > 0:
            k -= 1
        p += 1

    if s == 'P':
        if p > 0:
            p -= 1
        k += 1

print(k + p)



