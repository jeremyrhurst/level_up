# 11. Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

class Solution:
    def calculate_area(self, h1, h2, difference):
        return(min(h1, h2)*difference)
    
    def maxArea(self, heights: List[int]) -> int:
        first = 0
        last = len(heights) -1
        max_a = 0
        while first < last:
            cur = self.calculate_area(heights[first], heights[last], last-first)
            if cur > max_a:
                max_a = cur
            if heights[first] > heights[last]:
                last -= 1
            else:
                first += 1
        return max_a