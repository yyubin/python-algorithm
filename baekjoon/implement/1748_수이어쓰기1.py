import sys
n = int(sys.stdin.readline())
res = 0
len_ = len(str(n))

for i in range(len_-1):
    res += 9 * 10 ** i * (i+1)

print(res + (n - 10**(len_-1)+1) * len_)



# 메모리초과
# num = int(input())
# li = [str(i) for i in range(1, num+1)]
# print(len(''.join(li)))
#
#
