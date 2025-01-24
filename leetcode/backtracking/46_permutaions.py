'''
Given an array nums of distinct integers, return all the possible
permutations
. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]
'''

# The following is a recursive solution to the problem
# The base case is when the length of the list is 0, in which case we return an empty list
# The recursive case involves getting all the permutations of the list except the first element
# Inserts the first element into all possible positions in the permutations of the rest of the list
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return[[]]
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(0, len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res