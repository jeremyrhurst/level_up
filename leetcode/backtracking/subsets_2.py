'''
Subsets II

You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,1]

Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]

Example 2:

Input: nums = [7,7]

Output: [[],[7], [7,7]]

'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def recur(index, subset):
            if index >= len(nums):
                ans.append(subset[::])
                return
            subset.append(nums[index])
            recur(index+1, subset)

            subset.pop()
            # We can skip the duplicates becase we have already added them to the subset
            # This is the difference between subsets 1 and this problem
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            recur(index+1, subset)

        recur(0, [])    
        return ans