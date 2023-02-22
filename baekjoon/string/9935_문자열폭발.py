import sys
string = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

stack = []
last = bomb[-1]

for v in string:
    stack.append(v)
    if v == last and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

ans = ''.join(stack)
print('FRULA' if ans == '' else ans)


# while string != '':
#     if bomb not in string:
#         print(string)
#         break
#     string = string.strip(bomb)
# else:
#     print('FRULA')
#
