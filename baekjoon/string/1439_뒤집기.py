# import sys
# string = sys.stdin.readline().rstrip()
#
# if string == string[::-1]:
#     print(0)
# else:
#     if len(string) % 2 == 1:
#         left = list(string[:len(string)//2])
#         right = list(string[len(string)//2 + 1::])
#     else:
#         left = list(string[:len(string)//2])
#         right = list(string[len(string)//2::])
#
#     right = right[::-1]
#     cnt = 0
#     b = False
#
#     for i in range(len(left)):
#         if left[i] != right[i]:
#             if right[i] == right[i-1] and b:
#                 continue
#             cnt += 1
#             b = True
#         else:
#             b = False
#
#
#     print(cnt)


# import sys
# string = sys.stdin.readline().rstrip()
# li0 = 0
# li1 = 0
# b = False if string[0] == 0 else True
# for i in string:
#     if i == '0':
#         if b:
#             li0 += 1
#         b = False
#     elif i == '1':
#         if not b:
#             li1 += 1
#         b = True
#
#
# print(min(li0, li1))

import sys
string = sys.stdin.readline().rstrip()

count01 = string.count('01')
count10 = string.count('10')

print(max(count10, count01))
