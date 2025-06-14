import sys

def bs(x):
    start = 0
    end = int(1e9)

    res = []
    while start <= end:
        mid = (start + end) // 2
        three = (x - mid) // 2
        two = x - mid - three

        if two == three:
            three -= 1
            two += 1

        if mid > two > three:
            res = [mid, two, three]
            end = mid - 1
        elif two >= mid:
            start = mid + 1
        else:
            end = mid - 1
    return res

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    res = bs(n)
    print(res[1], res[0], res[2])
