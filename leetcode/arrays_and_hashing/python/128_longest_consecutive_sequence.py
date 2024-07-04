# Given an array of integers nums, return the length of the longest consecutive sequence of elements.
# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
# You must write an algorithm that runs in O(n) time.
# Example 1:
# Input: nums = [2,20,4,10,3,4,5]
# Output: 4

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Change nums into a set 
        # Start with a number that doesn't have a size smaller
        # While loop to find how many consecutive numbers are above starting number

        nset = set(nums)
        longest = 0
        for num in nset:
            if num-1 not in nset:
                length = 1
                while (num + length) in nset:
                    length += 1
                longest = max(longest, length)
        return(longest)