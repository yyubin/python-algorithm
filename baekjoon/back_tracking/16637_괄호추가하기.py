import sys
n = int(sys.stdin.readline())
li = sys.stdin.readline().rstrip()

op = (n-1) // 2
picked = [False] * op
ans = -sys.maxsize

def cal_part(a, oper, b):
    if oper =='+':
        return int(a) + int(b)
    elif oper =='*':
        return int(a) * int(b)
    else:
        return int(a) - int(b)

def cal():
    tmp = list(li)
    tmp_res = []
    visited = [False] * len(tmp)
    for j in range(op):
        if picked[j]:
            num = cal_part(tmp[j*2], tmp[j*2+1], tmp[j*2+2])
            visited[j*2] = True
            visited[j*2+1] = True
            visited[j*2+2] = True
            tmp_res.append(str(num))
        else:
            if not visited[j*2]:
                visited[j * 2] = True
                tmp_res.append(tmp[j*2])
            tmp_res.append(tmp[j*2+1])
            visited[j*2+1] = True

    if not visited[-1]:
        tmp_res.append(tmp[-1])

    if len(tmp_res) == 1:
        return int(tmp_res[0])

    last = int(tmp_res[0])
    for i in range(1, len(tmp_res)-1, 2):
        oper = tmp_res[i]
        rhs = int(tmp_res[i + 1])
        last = cal_part(last, oper, rhs)

    return last

def bt(idx):
    global ans
    if idx >= op:
        ans = max(ans, cal())
        return

    bt(idx+1)

    if idx == 0 or not picked[idx-1]:
        picked[idx] = True
        bt(idx+1)
        picked[idx] = False

bt(0)
print(ans)

## 마지막 숫자 추가 안했었음
# 만약 숫자가 하나밖에 없을 경우 0리턴하기 때문에 수정