import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
target = 1

for num in li:
    if target < num:
        break

    target += num

print(target)


#https://aerocode.net/392
#천재인둣 ㅡㅠㅜㅠㅜㅠㅡㅠㅜㅜㅠ

# weights - num in li 와 num - weights in li 부분에서
# 숫자가 여러번 사용가능해짐
# 아래 코드로 풀려면 가지고 있는 추와 가지고 있지 않은 추 계산하면서 해야함

# while True:
#     print(num)
#     if num > sum(li):
#         print(sum(li)+1)
#         sys.exit()
#
#     if num in li:
#         num += 1
#         continue
#
#     weights = li[0]
#     idx = 1
#
#     while True:
#         if weights == num:
#             break
#         if idx > len(li):
#             print(num)
#             sys.exit()
#         if num - weights in li:
#             break
#         if weights - num in li:
#             break
#         if weights < num:
#             weights += li[idx]
#             idx += 1
#         else:
#             print(num)
#             sys.exit()
#
#     num += 1



