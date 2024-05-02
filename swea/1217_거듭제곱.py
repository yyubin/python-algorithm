def square(num_, mul_):
    global ans
    ans = ans * num_
    mul_ -= 1
    if mul_ > 0:
        square(num_, mul_)
    else:
        return ans


for _ in range(10):
    tc = int(input())
    num, mul = map(int, input().split())
    ans = 1
    square(num, mul)
    print('#'+str(tc), ans)
