# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.


# The following is a cleaned up and more optimized version of the above code.
# The solution involves sorting the list and iterating through the list.
# For each element in the list, check if the sum of the element and the two pointers is equal to 0.
# If it is, add the elements to the result list.
# If the sum is less than 0, increase the middle pointer.
# If the sum is greater than 0, decrease the last pointer.
# If the last element is the same as the previous element, skip the element.
class Solution:
    def check(self, begin, middle, end, nums):
        ans = []
        last = None
        while middle < end:
            s = nums[begin] + nums[middle] + nums[end]
            if s == 0:
                # Skip if the last element is the same as the current element
                if nums[end] != last:
                    ans.append([nums[begin], nums[middle], nums[end]])
                    last = nums[end]
                end -= 1
                middle += 1
            elif s < 0:
                middle += 1
            else:
                end -= 1
        return (ans)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Iterate through all indexes of nums minus beginning and end
        # Check two sum with index -1, index, and index + 1
        ans = []
        nums.sort()
        last = None
        for i in range(0, len(nums)-2):
            # Skip if the last element is the same as the current element
            if last == nums[i]:
                continue
            last = nums[i]    
            res = self.check(i, i+1, len(nums)-1, nums)
            if len(res) != 0:
                ans.extend(res)
        return ans