#Given an integer array nums, return true if any value appears
# at least twice in the array, and return false if every element
# is distinct.

#Example 1:

#Input: nums = [1,2,3,1]
#Output: true

# Create a set and iterate through the list checking if the element is in the set
# Time complexity: O(n)
# Space complexity: O(n)
# 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prev = set()
        for num in nums:
            if num in prev:
                return True
            else:
                prev.add(num)
        return False
