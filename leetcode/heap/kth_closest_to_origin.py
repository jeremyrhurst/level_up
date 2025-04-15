
'''
K Closest Points to Origin
Solved

You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order.

Example 1:

Input: points = [[0,2],[2,2]], k = 1

Output: [[0,2]]

Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).

Example 2:

Input: points = [[0,2],[2,0],[2,2]], k = 2

Output: [[0,2],[2,0]]

Explanation: The output [2,0],[0,2] would also be accepted.

Constraints:

    1 <= k <= points.length <= 1000
    -100 <= points[i][0], points[i][1] <= 100


'''
# Minheap solution
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            minheap.append([dist,x,y])
        
        heapq.heapify(minheap)
        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(minheap)
            res.append([x,y])
        return res

