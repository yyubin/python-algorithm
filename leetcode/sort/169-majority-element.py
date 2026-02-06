from typing import List

# 과반수면 중앙값 반드시 과반값일 것
def majorityElement(self, nums: List[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]


# Boyer–Moore Majority Vote
# 과반수 존재하면 걍 다른거랑 짝지었을때 마지막까지 남는거 이용한 알고리즘
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        can = None
        cnt = 0

        for n in nums:
            if cnt == 0:
                can = n
            cnt += 1 if can == n else -1

        return can


# 원래 첫번째 방식으로 제출했는데 n log n 이고 통과는 함
# 보어 무어로 하는게 더 높게 나오는게 정상일텐데 실측에선 전자가 더 빠름
# 메모리는 이론상 두개 다 O(1)인데 전자가 정렬 과정에서 Timsort가 추가 공간을 써서 좀 낮게 나옴(O(n) 추가 공간)