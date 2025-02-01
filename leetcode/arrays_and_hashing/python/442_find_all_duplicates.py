'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:

Input: nums = [1,1,2]
Output: [1]

Example 3:

Input: nums = [1]
Output: []
'''

# Negative numbers are used to mark the presence of a number in the list
# If the number is already negative, it is a duplicate
# If the number is not negative, make it negative
# add the number to the list of duplicates
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                ans.append(abs(nums[i]))
            nums[abs(nums[i])-1] *= -1
        return ans