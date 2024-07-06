# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        l = 0
        r = len(height) -1
        lmax = height[l]
        rmax = height[r]
        while l < r:
            if height[l] < height[r]:
                if height[l] < lmax:
                    area += lmax - height[l]
                if height[l] > lmax:
                    lmax = height[l]
                l += 1
            else:
                if height[r] < rmax:
                    area += rmax - height[r]
                if height[r] > rmax:
                    rmax = height[r]
                r -= 1
        return area