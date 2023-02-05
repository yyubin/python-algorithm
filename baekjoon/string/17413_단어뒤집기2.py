# import sys
# string = list(sys.stdin.readline().rstrip())
# result = []
#
# while '<' in string:
#     a = string.index('<')
#     b = string.index('>')
#
#     tmp_a = string[:a]
#     for i in range(len(tmp_a)-1):
#         if tmp_a[i] == ' ':
#             result.append(tmp_a[:int(i)-1:-1])
#             result.append([' '])
#
#             for j in tmp_a[:i:-1]:
#                 tmp_a.remove(j)
#             print(result)
#
#     tmp = string[a:b+1]
#     result.append(tmp)
#
#     for i in tmp:
#         string.remove(i)
#
# print(result)

import sys
string = list(sys.stdin.readline().rstrip())
flag = False
stack1 = ''
stack2 = ''

for i in string:
    if not flag:
        if i == '<':
            flag = True
            stack1 += i
        elif i == ' ':
            stack1 += i
            stack2 += stack1
            stack1 = ''
        else:
            stack1 = i + stack1
    elif flag:
        stack1 += i
        if i == '>':
            flag = False
            stack2 += stack1
            stack1 = ''


print(stack2+stack1)


