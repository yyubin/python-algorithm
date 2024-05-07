#11399번
# num = int(input())
# list1 = list(map(int, input().split()))
#
# list1.sort()
# sum = 0
# for i in range(0, len(list1)):
#     sum += list1[i]*num
#     num -= 1
# print(sum)

#1920번
#100,000 범위이므로 nlogn 시간안에 오는 알고리즘써야함
# import sys
# n = int(sys.stdin.readline().rstrip())
# n_list = list(map(int, sys.stdin.readline().rstrip().split()))
# m = int(sys.stdin.readline().rstrip())
# m_list = list(map(int, sys.stdin.readline().rstrip().split()))
#
# for i in range(0, m):
#     if m_list[i] in n_list:
#         print(1)
#     else:
#         print(0)

# 같은 풀이지만 스킬이 모자란듯

# from sys import stdin, stdout
# n = stdin.readline()
# N = set(stdin.readline().split())
# m = stdin.readline()
# M = stdin.readline().split()
#
# for l in M:
#     stdout.write('1\n') if l in N else stdout.write('0\n')

#2812번 골드3
# from sys import stdin
# import re
# a, b = map(int, stdin.readline().split())
# num = stdin.readline()
# n_list = re.findall(r'\d', num)
# n_list = [int (i) for i in n_list]
# while b > 0:
#     n_list.remove(min(n_list))
#     b -= 1
# print(*n_list, sep='')
## 실패 ㅠㅠ

#1026번
# from sys import stdin
# num = int(stdin.readline())
# list_a = list(map(int, stdin.readline().split()))
# list_b = list(map(int, stdin.readline().split()))
# sum = 0
# for i in range (0, num):
#     sum += min(list_a)*max(list_b)
#     list_a.remove(min(list_a))
#     list_b.remove(max(list_b))
# print(sum)

#2217번
# from sys import stdin
# num = int(stdin.readline())
# list_a = []
# list_b = []
# for i in range(0, num):
#     list_a.append(int(stdin.readline()))
#
# list_a.sort(reverse=True)
#
# for i in range(0, num):
#     list_b.append(list_a[i]*(i+1))
#
# print(max(list_b))

# 10 15 20 이 있으면 x인 중량을 들어올릴때 각각 받는 중량이 x/3이 됨
# 몇 개만 사용해도 됨
# 10 15 20에 x가 30이면 혼자서는 못든다 max(list_a)
# 30까지는 들수 있음
# 40 일 경우 40%3 13.333 --> 불가

#14425번
from sys import stdin
num1, num2 = map(int, stdin.readline().split())
list_a = []
list_b = []
for i in range(0, num1):
    list_a.append(stdin.readline().rstrip())
for i in range(0, num2):
    temp = (stdin.readline().rstrip())
    if temp in list_a:
        list_b.append(temp)

print(len(list_b))






