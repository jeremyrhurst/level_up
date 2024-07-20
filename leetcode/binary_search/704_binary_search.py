# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# My own solution using recursion and three pointers
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # be passed begin, cur, and end
        # if current index == target return
        # if current index is larger than target
        # recur on begin to 1 behind cur
        # if current index is smaller than target
        # recur on cur +1 to end
        def recur(begin, cur, end):
            if nums[cur] == target:
                return cur
            if begin == cur == end:
                return -1
            if nums[cur] > target:
                return recur(begin, (begin + (cur-1))//2, cur-1)
            else:
                return recur(cur+1, (cur+1+end)//2, end)
        return recur(0, len(nums)//2, len(nums)-1)

# neetcode solution using while loop
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1