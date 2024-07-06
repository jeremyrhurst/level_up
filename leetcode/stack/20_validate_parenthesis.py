# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        parens = {'{':'}','[':']','(':')'}
        stack = []
        for p in s:
            if p in parens.keys():
                stack.append(parens[p])
            else:
                if len(stack) == 0 or stack.pop() != p:
                    return False
        if len(stack) == 0:
            return True
        return False