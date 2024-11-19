'''
78. Subsets
Medium

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

 

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.


'''

# This is a backtracking problem
# The idea is to choose a number and then recur on the rest of the numbers
# Copy the subset and append the number to the subset
class Solution:
      # 1           -1
      # 2    -2     2  -2
      # 3 -3 3 -3 3 -3 3 -3
      # [1,2,3][1,2][1,3][1][2,3][2][3][]
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        def recur(index):
            if index >= len(nums):
                # Add a copy of the subset to the ans
                # we need to use copy here because subset is a reference to the same list
                # if we don't use copy, the list will be empty at the end
                ans.append(subset.copy())
                return
            # chose first recur on rest
            subset.append(nums[index])
            recur(index+1)
            # don't chose first, recur on rest
            subset.pop()
            recur(index+1)
        recur(0)
        return ans