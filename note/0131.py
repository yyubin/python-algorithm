import sys
# li = list(map(int, sys.stdin.readline().rstrip().split()))
#
# if li[0] == li[1] == li[2]:
#     print(10000 + li[0]*1000)
# elif li[0] != li[1] != li[2] != li[0]:
#     print(max(li) * 100)
# else:
#     if li[0] == li[1] or li[0] == li[2]:
#         print(1000 + li[0]*100)
#     elif li[1] == li[2]:
#         print(1000 + li[1]*100)


a = input()
li = list(map(int, sys.stdin.readline().rstrip().split()))
num = int(input())
print(li.count(num))
