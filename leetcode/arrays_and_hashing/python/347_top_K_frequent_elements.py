# 347. Top K Frequent Elements
# Medium
# 
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# 
# Example 1:
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# My own solution using a frequency array
# This solution works but is slow and can be optimized
# Since this soulution finds the max value in the frequency array and then finds the index of that value
# The time complexity is O(n^2) where n is the number of elements in the nums array
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a frequency array with a size of the highest value
        highest_value = max(nums)
        smallest_value = min(nums)
        count = [0]*(highest_value - smallest_value+1)
        for num in nums:
            count[num-smallest_value] += 1
        
        # Find the largest freq in array and add index to ans array
        # Set value of freq array to 0 for that index
        # repeat until ans array is as long as k
        ans = []
        while len(ans) < k:
            cur_max = max(count)
            max_index = count.index(cur_max)
            ans.append(max_index+smallest_value)
            count[max_index] = 0
        return ans

# Solution using bucket sort and a frequency dictionary
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a frequency dictionary for the nums array
        count = {}
        # Create a frequency array with a size of the length of the nums array
        freq = [[] for i in range(len(nums)+1)]

        # Create a frequency dictionary for the nums array and add the frequency to the freq array
        # key: num, value: frequency
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for key, value in count.items():
            freq[value].append(key)
        
        ans = []

        # Add the elements in the freq array to the ans array in descending order
        # until the length of the ans array is equal to k
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        