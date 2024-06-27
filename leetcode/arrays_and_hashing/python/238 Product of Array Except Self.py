class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        # prefix array
        prev = 1
        for i in range(len(nums)):
            ans[i] = prev
            prev *= nums[i]
        last = 1
        for i in range(len(ans)-1, -1, -1):
            ans[i] = last*ans[i]
            last *= nums[i]
        return ans  