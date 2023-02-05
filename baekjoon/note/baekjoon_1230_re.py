# 17478번 재귀함수가 뭔가요?
# cnt = int(input())
#
# print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
# num = 0
#
#
# def speak(cnt: int, num: int):
#     print("__" * num * 2, end="")
#     print('"재귀함수가 뭔가요?"')
#     if num == cnt:
#         print("__" * num * 2, end="")
#         print('"재귀함수는 자기 자신을 호출하는 함수라네"')
#         print("__" * num * 2, end="")
#         print('라고 답변하였지.')
#         return
#     print("__" * num * 2, end="")
#     print('"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
#     print("__" * num * 2, end="")
#     print('마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
#     print("__" * num * 2, end="")
#     print('그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
#     speak(cnt, num + 1)
#     print("__" * num * 2, end="")
#     print('라고 답변하였지.')
#
#
# speak(cnt, num)

# 18511번 큰 수 구성하기
# from itertools import product
#
# n, k = map(int, input().split())
# li = list(map(str, input().split()))
# num = len(str(n))
#
# def find(cnt: int):
#     for _ in printList:
#         string = int("".join(printList[cnt]))
#         if string <= n:
#             li2.append(string)
#         cnt -= 1
#
# li2 = []
# for i in range(num):
#     printList = list(product(li, repeat=num-i))
#     cnt = len(printList) - 1
#     find(cnt)
#
# print(max(li2))

# 22460번 : 특별상이라도 받고 싶어
# n = int(input())
# li = []
#
# for i in range(n):
#     li.append(list(map(int, input().split())))
#

# 23304번 : 아카라카
# string = input()
# cnt = 0
#
#
# def check(s):
#     global cnt
#
#     s1 = s[:len(s) // 2]
#     s2 = s[len(s) // 2 if len(s) % 2 == 0
#            else ((len(s) // 2) + 1):]
#     if s2[::-1] != s1 or s1 != s2:
#         pass
#     else:
#         if len(s1) > 2:
#             check(s1)
#             check(s2)
#         else:
#             cnt += 1
#             return
#
# check(string)
# if cnt > 0:
#     print("AKARAKA")
# else:
#     print("IPSELENTI")

# 소수&팰린드롭
# import math
#
# num = int(input())
# result = 0
#
# def is_prime_number(x):
#     for i in range(2, int(math.sqrt(x)) + 1):
#         if x % i == 0:
#             return False
#     return True
#
#
# for i in range(num, 1000001): # 범위 고려해 줄것
#     if i == 1:
#         continue
#     if str(i) == str(i)[::-1]:
#         if is_prime_number(i):
#             result = i
#             break
#
# if result == 0:
#     result = 1003001 # 예외처리..ㅠㅠ
#
# print(result)

# 단어 뒤집기 2
import re

string = input()
li = []
s1 = ''
s2 = ''
find_left = []
find_right = []

if string.find('<') == -1:
    pass
else:
    for text in re.finditer('<', string):
        find_left.append(text.start())
    for text in re.finditer('>', string):
        find_right.append(text.start())
    print(find_right, find_left)


if s1 != '':
    print(s1, end='')
for i in li:
    print(i[::-1], end=' ')

if s2 != '':
    print(s2)


