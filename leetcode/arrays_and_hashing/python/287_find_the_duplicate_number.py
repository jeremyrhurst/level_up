'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
'''

# Negative numbers are used to mark the presence of a number in the list
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                return abs(nums[i])
            nums[abs(nums[i])-1] *= -1

# Fast and slow pointer solution:
# The idea is to treat the list as a linked list with the value at the index as the next node
# The fast pointer moves twice as fast as the slow pointer
# When the two pointers meet, we reset the slow pointer to the beginning of the list
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


# Binary search solution:
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                high = mid
            else:
                low = mid + 1
        return low