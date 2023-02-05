import sys

n = int(sys.stdin.readline().rstrip())
boxes = list(map(int, sys.stdin.readline().rstrip().split()))

d = [1] * n

for i in range(1, n):
    for j in reversed(range(i)):
        if boxes[i] > boxes[j]:
            d[i] = max(d[i], d[j]+1)

print(max(d))





# li = [boxes[0]]


# def dynamic(x):
#     global li
#     print(li)
#     max_ = max(li)
#     if x > max_:
#         li.append(x)
#     elif x <= max_:
#         for k, v in enumerate(li):
#             if v > x:
#                 li = li[:k]
#         li.append(x)
#
#
# for i in range(1, len(boxes)):
#     dynamic(boxes[i])
#
# print(li)

# cnt = 2
# now_in = boxes[0]
# now_out = boxes[1]
# li = []
# for i in boxes:
#     if now_in < i:
#         if now_out > i:
#             now_out = i
#         elif now_out < i:
#             print(now_in, now_out)
#             now_in = now_out
#             now_out = i
#             cnt += 1
