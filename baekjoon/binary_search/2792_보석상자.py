import sys
n, m = map(int, sys.stdin.readline().split())
li = [int(sys.stdin.readline()) for _ in range(m)]

start = 1
end = max(li)

result = 0

while start <= end:
    mid = (start+end)//2
    tmp = 0
    for i in li:
        tmp += i//mid
        if i%mid != 0:
            tmp += 1

    if tmp > n:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)

## mid가 질투심
# 사탕 돌면서 나눠줌
# 근데 최대한 같은 숫자로 나눠줘야함(헉생하나당 같은 색상의 사탕만 가질수있음)
# tmp가 만약 n보다 작으면 사탕을 못가지는 학생이 나오는것 (학생은 반드시 1개 이상의 사탕을 가져야한다)
# 만약 현재 질투심(그니까 나눠줄 사탕의 개수이자 최대 질투심)이 0으로 안나눠 떨어진다는 건?? 남은 개수는 다른 사람한테 몰아줘하는것 그니까
# 그 색상의 사탕을 가지는 학생이? 한명더생기는거

