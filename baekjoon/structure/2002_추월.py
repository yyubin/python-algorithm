import sys
n = int(sys.stdin.readline())
in_ = [sys.stdin.readline().rstrip() for _ in range(n)]
out_ = [sys.stdin.readline().rstrip() for _ in range(n)]
res = 0
for i in range(n):
    if in_[i] != out_[i]:
        res += 1
        idx = in_.index(out_[i])
        in_.insert(i, in_.pop(idx))
print(res)