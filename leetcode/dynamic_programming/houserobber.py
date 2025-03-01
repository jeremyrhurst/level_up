
'''
House Robber

You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:

Input: nums = [1,1,3,3]

Output: 4

Explanation: nums[0] + nums[2] = 1 + 3 = 4.

Example 2:

Input: nums = [2,9,8,3,6]

Output: 16

Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 100

'''
# Dynamic programming approach
class Solution:
    def rob(self, nums: List[int]) -> int:
       if len(nums) == 1:
            return nums[0]
       #  Get max of previous and compare next  
       maxn = [0]* len(nums)

       maxn[0] = nums[0]
       maxn[1] = max(nums[0], nums[1])
       for i in range(2, len(nums)):
          maxn[i] = max(nums[i] + maxn[i-2], maxn[i-1])
       return maxn[-1]

# Tabulation approach
class Solution:
    def rob(self, nums: List[int]) -> int:
       #  Get max of previous and compare next  
       maxn = [0]* len(nums)

       maxn[0] = nums[0]
       if len(nums) > 1:
          maxn[1] = max(nums[0], nums[1])
       for i in range(2, len(nums)):
          maxn[i] = max(nums[i] + maxn[i-2], maxn[i-1])
       return maxn[-1]

# Recursion approach/ memoization approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums, i, memo):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] + helper(nums, i-2, memo), helper(nums, i-1, memo))
            return memo[i]
        return helper(nums, len(nums)-1, {})

# Dynamic programming approach space optimized
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Get max of previous and compare next
        prev1 = 0
        prev2 = 0
        for num in nums:
            temp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = temp
        return prev1