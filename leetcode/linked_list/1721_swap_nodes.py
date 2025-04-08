'''
1721. Swapping Nodes in a Linked List
Solved
Medium
Topics
Companies
Hint

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

 

Constraints:

    The number of nodes in the list is n.
    1 <= k <= n <= 105
    0 <= Node.val <= 100
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        begin = head
        last = begin
        middle = last
        # k-1 because if we want the kth node from the beginning, we need to move k-1 times
        for i in range(k-1):
            last = last.next
            begin = begin.next
        while last.next:
            last = last.next
            middle = middle.next
        # Swap begin and middle
        temp = begin.val
        begin.val = middle.val
        middle.val = temp
        return head

# Solution for swapping the head with kth node from the end
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        begin = head
        last = begin
        middle = last
        for i in range(k-1):
            last = last.next
        while last.next:
            last = last.next
            middle = middle.next
        # Swap begin and middle
        temp = begin.val
        begin.val = middle.val
        middle.val = temp
        return head
