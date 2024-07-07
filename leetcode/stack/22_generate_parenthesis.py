# 22. Generate Parentheses
# Medium
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 
# Example 1:
# 
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# 
# Example 2:
# 
# Input: n = 1
# Output: ["()"]


from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        stack = []
        def backtrack(openn, closedn):
            # if we have n open and n closed brackets, we have a valid combination
            if openn == closedn == n:
                ans.append(''.join(stack))
            # if we have less than n open brackets, we can add an open bracket
            if openn < n:
                stack.append('(')
                backtrack(openn + 1, closedn)
                # Pop because we are working with only one stack and we need to backtrack
                stack.pop()
            # if we have less closed brackets than open brackets, we can add a closed bracket
            if closedn < openn:
                stack.append(')')
                backtrack(openn, closedn + 1)
                stack.pop()

        backtrack(0,0)
        return ans
