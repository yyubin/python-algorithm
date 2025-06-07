import sys
def is_even(num):
    if num % 2 == 0:
        return True
    return False

for _ in range(int(sys.stdin.readline())):
    n, m, k = map(int, sys.stdin.readline().split())
    nn, mm, kk = is_even(n), is_even(m), is_even(k)
    if nn:
        if kk:
            print("YES")
        else:
            print("NO")
    else:
        hori = m//2
        if k < hori:
            print("NO")
        elif (k-hori) % 2 == 0:
            print("YES")
        else:
            print("NO")

