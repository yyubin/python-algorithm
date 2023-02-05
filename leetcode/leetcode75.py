from collections import deque
from typing import Optional


#Day 2

def isIsomorphic(s: str, t: str) -> bool:
    dic_s = {}
    dic_t = {}
    key_s = 0
    key_t = 0
    list_s = []
    list_t = []
    for i in range(0, len(s)):
        if s[i] not in dic_s:
            dic_s[s[i]] = key_s
            key_s += 1
        if t[i] not in dic_t:
            dic_t[t[i]] = key_t
            key_t += 1

    for i in range(0, len(s)):
        dic_s.get(s[i])
        list_s.append(dic_s.get(s[i]))
        dic_t.get(t[i])
        list_t.append(dic_t.get(t[i]))

    return list_s == list_t

# print(isIsomorphic("foo","bar"))

# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         dic = {}
#         #150은 아스키코드 갯수. 이미 들어와있는데 dic에 추가하면 False를 리턴
#         check = [False] * 150
#         for i in range(len(s)):
#             if s[i] not in dic :
#                 if check[ord(t[i])] == True:
#                     return False
#                 dic[s[i]] = t[i]
#                 check[ord(t[i])] = True
#             else :
#                 if dic[s[i]] != t[i]:
#                     return False
#         return True

def isSubsequence(s: str, t: str) -> bool:
    i, j = 0, 0
    # 투 포인터 개념인듯
    # 우선 s가 길수도 있고 t가 길수도 있음

    while i < len(s) and j < len(t):
        # 두개 중 뭐가 더 길지는 모름 둘다 끝나야함
        # 우선 0부터 시작해서 각각 비교함
        # 겹치는게 없으면 j를 증가시켜서 t의 포인터 이동
        # 겹치는게 있으면 i와 j 모두 증가 시킴
        # while문이 종료되었을 때, len(s)와 i가 같다면 모든 순서에 맞는 문자가 j안에 있었음을 알 수 있다
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1

    if len(s) == i:
        return True
    return False

#print(isSubsequence("leeeeetcode","db"))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    node = ListNode(0)
    cur = node
    print(node.val)
    print(l1)
    # while l1 and l2:
    #     if l1.val <= l2.val:
    #         cur.next = l1
    #         l1 = l1.next
    #     else:
    #         cur.next = l2
    #         l2 = l2.next
    #     cur = cur.next
    # cur.next = l1 or l2

    return node.next

print(mergeTwoLists([1,2,4],[1,3,4]))