# 739. Daily Temperatures
# Medium
# 
# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
# 
# Example 1:
# 
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Create the result array with all zeros
        res = [0] * len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                # Pop the top of the stack
                s_index, s_val = stack.pop()
                # Since we know the temp of the current day is greater than the temp of the day at the top of the stack, we can calculate the difference in days
                # And add it to the result array
                res[s_index] = i - s_index
            # Append the current day to the stack both index and value
            stack.append((i, val))
        return res