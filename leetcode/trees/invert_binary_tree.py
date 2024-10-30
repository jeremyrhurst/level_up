# 226. Invert Binary Tree
# Easy
# 
# Given the root of a binary tree, invert the tree, and return its root.
# 
# Example 1:
# 
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# 
# Example 2:
# 
# Input: root = [2,1,3]
# Output: [2,3,1]
# 
# Example 3:
# 
# Input: root = []
# Output: []

# My own solution
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        # call invertTree on children
        # perform swap
        def swap(node):
            temp = node.left
            node.left = node.right
            node.right = temp

        def recur(node):
            # Base case
            # check if left and right
            # recur on both
            # swap left and right
            if not node.left and not node.right:
                return node
            if node.left:
                recur(node.left)
            if node.right:
                recur(node.right)
            swap(node)
            return node
        return recur(root)

# Solution with simple few lines
# Same time and memory as my solution

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
