# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Brute force solution involves
# two for loops to iterate over the list and check if the sum of the two numbers is equal to the target.
# If it is, return the indices of the two numbers.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:], i+1):
                if num1 + num2 == target:
                    return [i, j]

# Optimized solution involves using a dictionary to store the previous numbers and their indices.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = {}
        for i in range(len(nums)+1):
            if (target - nums[i]) in prev_nums.values():
                return[i,list(prev_nums.keys())[list(prev_nums.values()).index(target-nums[i])]]
            else:
                prev_nums[i] = nums[i]

# The following is a cleaned up and more optimized version of the above code.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = {}
        for i, num in enumerate(nums):
            if (target - num) in prev_nums:
                return [prev_nums[target - num], i]
            prev_nums[num] = i