# import sys
#
# n = int(sys.stdin.readline())
# result = []
#
# def two_pointers(string: list):
#     a, b = 0, len(string) - 1
#     while a < b:
#         if string[::-1] == string:
#             return 0
#         if string[a] == string[b]:
#             a += 1
#             b -= 1
#         elif string[a + 1] == string[b] or string[a] == string[b - 1]:
#             temp1 = string[a + 1:b + 1]
#             temp2 = string[a:b]
#             if temp1 == temp1[::-1]:
#                 del string[a]
#                 a += 1
#                 return 1
#             elif temp2 == temp2[::-1]:
#                 del string[b]
#                 b -= 1
#                 return 1
#         else:
#             return 2
#
#
# for _ in range(n):
#     print(two_pointers(list(sys.stdin.readline().strip())))
#

# 시간초과..

import math

t = int(input())

for _ in range(t):
    data = input()

    if data == data[::-1]:
        print("0")

    else:
        data_start = list(data)
        data_end = list(data)

        for i in range(math.ceil(int(len(data) / 2))):

            if data[i] != data[-(i + 1)]:
                data_start.pop(i)
                data_end.pop(-(i + 1))

                if data_start == data_start[::-1]:
                    print("1")
                    break

                if data_end == data_end[::-1]:
                    print("1")
                    break

                print("2")
                break
