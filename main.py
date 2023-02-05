# This is a sample Python script.
from typing import List


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# Leetcode 1480
def runningSum(nums: List[int]) -> List[int]:
    list1 : List[int] = []
    list1 = [sum(nums[:i]) for i in range(1, len(nums)+1)]

    return list1

#runningSum(nums=[1,2,3,4])

# Leetcode 724.Find Pivot Index
def pivotIndex(nums: List[int]) -> int:
    left = 0
    total = sum(nums)

    for i, x in enumerate(nums):
        print(left, total-x-left)
        if left == total - left - x :
            return i
        left += x
    return -1



print(pivotIndex([1,7,3,6,5,6]))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
