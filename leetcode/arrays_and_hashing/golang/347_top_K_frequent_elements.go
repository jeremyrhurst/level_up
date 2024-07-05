/*
347. Top K Frequent Elements
Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
*/

// Bucket Sort Solution
// Time: O(n)
// Space: O(n)

func topKFrequent(nums []int, k int) []int {
	// Create a map to store the count of each number
	m := make(map[int]int)
	// Iterate through the numbers and increment the count in the map
	for _, n := range nums {
		m[n]++
	}
	// Create a slice of buckets to store the numbers with the same count
	buckets := make([][]int, len(nums)+1)
	// Iterate through the map and add the numbers to the corresponding bucket
	for n, c := range m {
		// Append the number to the bucket with the count as the index
		buckets[c] = append(buckets[c], n)
	}
	// Create a slice to store the result
	res := make([]int, 0)
	// Iterate through the buckets in reverse order
	for i := len(buckets) - 1; i >= 0; i-- {
		if len(buckets[i]) > 0 {
			// Append the numbers from the bucket to the result
			res = append(res, buckets[i]...)
		}
		// Break if the result has k elements
		if len(res) >= k {
			break
		}
	}
	// Return the first k elements of the result
	return res[:k]

}