# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []
        for i, height in enumerate(heights):
            # Start of the histogram is the current index i if the stack is empty
            start = i
            # while the current is less than the previous
            # Pop the top of to stack, calcalate area for previous
            while stack and stack[-1][0] > height:
                lheight, li = stack.pop()
                area = lheight * (i-li)
                if area > largest:
                    largest = area
                # start of the histogram is the index of the previous element in the stack if the stack is not empty
                start = li
            stack.append([height,start])
        # Calculate the area for the remaining elements in the stack
        # The area is the height of the element times the width of the histogram
        # The width of the histogram is the length of the heights array minus the index of the element
        # The index of the element is the second element in the tuple
        # The height of the element is the first element in the tuple
        for h, i in stack:
            area = h * (len(heights)- i)
            if area > largest:
                largest = area
        return largest