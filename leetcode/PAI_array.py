from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i
        # {2: 0, 7: 1, 11: 2, 15: 3}

    for i, num in enumerate(nums): # 0, 2
        if target - num in nums_map and i != nums_map[target-num]:
        # 9 - 2 = 7 , nums_map의 키가 7인 값이 존재함 이때의 value는 1
        # 그리고 0이 nums_map[7]의 값이 아니어야함  -> 자기 자신이 아니어야함
            return [i, nums_map[target-num]]
            # 그때 0, nums_map[7]을 리턴
            # [0,1]


print(twoSum([2,7,11,15], 9))