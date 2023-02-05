# 떡볶이 떡 자르기
# num, height = map(int, input().split())
# li = list(map(int, input().split()))
#
# def binary_search(array, target, start, end) :
#     global mid
#     while start <= end:
#         mid = (start + end) // 2
#         li2 = [0 if i - mid < 0 else i - mid for i in array] #나열된 떡들에서 한 지점을 기준으로 길이를 뺐음
#         # start = 10 end = 19 였는데
#         # end = mid - 1 --> start = 10, end = 13, mid = 11
#         print("mid", mid)
#         print(li2)
#         print(sum(li2))
#
#         if sum(li2) == target:
#             return mid
#         elif sum(li2) > target:
#             start = mid + 1
#         else:
#             end = mid - 1
#
#     return mid
#
# result = binary_search(li, height, 0, max(li))
# print(result)


# 그니까, 떡 최소길이 ~ 최대길이 사이에서 하나 골라서
# 잘랐는데 그게 height랑 가까우면 그걸 리턴하면 됨

# 추가로 최대한 덜 잘랐을 때가 답이므로 덜잘랐을 경우 mid값을 저장해주면서 진행해야 한다!!
# 나머진 맞춰써~~


# 정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_left, bisect_right

def bisect(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

n, m = map(int, input().split())
li = list(map(int, input().split()))

print(bisect(li, m, m))






