# li = list(map(int, input().split()))
# result = 0
#
# for i in range(len(li) - 1):
#     if i == len(li) - 1:
#         break
#     if li[i] < li[i + 1]:
#         result += 1
#     else:
#         result -= 1
#
# if result == len(li) - 1:
#     print("ascending")
# elif result == (len(li) - 1) * -1:
#     print("descending")
# else:
#     print("mixed")


# a, b = input().split()
#
# if int(a[::-1]) > int(b[::-1]):
#     print(int(a[::-1]))
# else:
#     print(int(b[::-1]))

# li = list(map(int, input().split()))
# s = 0
# for i in li:
#     s += i * i
# print(s % 10)


import collections
import re

li = input()
li = li.lower()

dic = {}

for i in li:
    if i not in dic:
        dic[i] = 0
    else:
        dic[i] += 1

max_keys = [key for key, value in dic.items() if value == max(dic.values())]
if len(max_keys) > 1:
    print('?')
else:
    print(max_keys[0].upper())
