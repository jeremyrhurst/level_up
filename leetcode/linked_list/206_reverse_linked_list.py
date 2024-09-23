# Easy
# 
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# 
#  
# 
# Example 1:
# 
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# 
# Example 2:
# 
# Input: head = [1,2]
# Output: [2,1]
# 
# Example 3:
# 
# Input: head = []
# Output: []


# Iterative solution
# We keep track of the previous node and the current node
# We iterate through the linked list and reverse the next pointer of the current node
# We then move the previous node to the current node and the current node to the next node
# We return the previous node as the new head of the linked list
# Time complexity is O(n) where n is the number of nodes in the linked list
# Space complexity is O(1) as we are using constant space
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev