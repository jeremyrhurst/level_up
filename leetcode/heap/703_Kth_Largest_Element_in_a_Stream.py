'''
You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

Implement the KthLargest class:

    KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
    int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.

 

Example 1:

Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

Output: [null, 4, 5, 5, 8, 8]

Explanation:

KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3); // return 4
kthLargest.add(5); // return 5
kthLargest.add(10); // return 5
kthLargest.add(9); // return 8
kthLargest.add(4); // return 8

Example 2:

Input:
["KthLargest", "add", "add", "add", "add"]
[[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]

Output: [null, 7, 7, 7, 8]

Explanation:
KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
kthLargest.add(2); // return 7
kthLargest.add(10); // return 7
kthLargest.add(9); // return 7
kthLargest.add(9); // return 8

 

Constraints:

    0 <= nums.length <= 104
    1 <= k <= nums.length + 1
    -104 <= nums[i] <= 104
    -104 <= val <= 104
    At most 104 calls will be made to add.
'''

class KthLargest:

    # The constructor initializes the kth largest element in the stream.
    # It uses a min-heap to keep track of the k largest elements.
    # The add method adds a new score to the stream and returns the kth largest element.
    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)
        # If the size of the heap exceeds k, we remove the smallest element.
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)
        

    # The add method adds a new score to the stream.
    # If the new score is larger than the smallest element in the min-heap,
    # it replaces the smallest element with the new score.
    # Finally, it returns the kth largest element, which is the smallest element in the min-heap.
    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        # If the size of the heap exceeds k, we remove the smallest element.
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
        