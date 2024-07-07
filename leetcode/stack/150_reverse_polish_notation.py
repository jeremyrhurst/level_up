# 150. Evaluate Reverse Polish Notation
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
# 
# Evaluate the expression. Return an integer that represents the value of the expression.
# 
# Note that:
# 
#     The valid operators are '+', '-', '*', and '/'.
#     Each operand may be an integer or another expression.
#     The division between two integers always truncates toward zero.
#     There will not be any division by zero.
#     The input represents a valid arithmetic expression in a reverse polish notation.
#     The answer and all the intermediate calculations can be represented in a 32-bit integer.
# 
# Example 1:
# 
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# 
# Example 2:
# 
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# Approach:
# 1. We will use a stack to store the operands.
# 2. We will iterate through the tokens.
# 3. If the token is an operand, we will push it onto the stack.
# 4. If the token is an operator, we will pop the top two elements from the stack.
# 5. We will perform the operation and push the result back onto the stack.
# 6. Finally, we will return the top element from the stack.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(token))
        return stack[0]
