# 155. Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# 
#     MinStack() initializes the stack object.
#     void push(int val) pushes the element val onto the stack.
#     void pop() removes the element on the top of the stack.
#     int top() gets the top element of the stack.
#     int getMin() retrieves the minimum element in the stack.
# 
# You must implement a solution with O(1) time complexity for each function.
# 
# Example 1:
# 
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# Output
# [null,null,null,null,-3,null,0,-2]
# 
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

# Since there is no constraint on space complexity, we can use an additional stack to store the minimum values.
# The only constraint is constant time complexity for each function.
class MinStack:

    def __init__(self):
        self.stack =[]
        self.m = []

        

    # When we push onto the stack we want to also check 
    # if the value is less than or equal to the current minimum value
    def push(self, val: int) -> None:
        if len(self.m) == 0 or self.m[-1] >= val:
            self.m.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        # if we are popping the minimum value, we also want to pop from the minimum stack
        cur = self.stack.pop()
        if cur == self.m[-1]:
            self.m.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.m[-1]
