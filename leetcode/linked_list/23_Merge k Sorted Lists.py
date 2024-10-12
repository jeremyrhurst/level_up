import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# First solution using mergeTwoLists function and recursion
# Divide and conquer
# Divide: Split the list of linked lists into two halves and recursively merge them
# Conquer: Merge the two halves
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        # Devide and conquer use recursion
        # It is possible to use iteration here, just iterate through the input
        # list and merge two lists at a time

        if (not lists or len(lists) == 0):
            return None
            
        # Solution from pre
        def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
            dummy = node = ListNode()

            while list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                node = node.next

            node.next = list1 or list2

            return dummy.next

        def helper(lists, left, right):
            if left == right:
                return lists[left]

            # divide
            mid = (left + right) //2
            lefthead = helper(lists, left, mid)
            righthead = helper(lists, mid+1, right)

            # conquer
            mergedhead = mergeTwoLists(lefthead, righthead)
            return mergedhead
        
        return helper(lists, 0, len(lists) - 1)


# Solution using a min heap
# We use a min heap to keep track of the smallest element in each list
# We push the first element of each list into the heap
# We pop the smallest element from the heap and add it to the result list
# We then push the next element from the list of the popped element into the heap
# We repeat this process until the heap is empty
# Time complexity is O(nlogk) where n is the total number of elements in all the lists and k is the number of lists
# The reason we use a min heap for this is because we want to keep track of the smallest element in each list at all times so that we can merge them in sorted order
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Definition for singly-linked list.
        # Devide and conquer use recursion
        # It is possible to use iteration here, just iterate through the input
        # list and merge two lists at a time

        if (not lists or len(lists) == 0):
            return None

        # Solution from pre
        def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
            dummy = node = ListNode()

            while list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                node = node.next

            node.next = list1 or list2

            return dummy.next

        # Solution using a min heap
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = node = ListNode()
        while heap:
            val, i, node = heapq.heappop(heap)
            dummy.next = node
            dummy = dummy.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))



