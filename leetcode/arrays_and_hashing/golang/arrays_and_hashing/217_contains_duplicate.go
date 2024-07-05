/*
217. Contains Duplicate
Easy

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
*/

// Time: O(n)
// Space: O(n)
// Hash Table Solution
package main
func containsDuplicate(nums []int) bool {
	// Create a map to store the numbers
	// The key is the number and the value is a boolean
	// to indicate if the number is already in the map
	m := make(map[int]bool)
	// Iterate through the numbers and check if the number is already in the map
	for _, num := range nums {
		// If the number is already in the map, return true
		if _, ok := m[num]; ok {
			return true
		}
		// Otherwise, add the number to the map
		m[num] = true
	}
	// If no number is repeated, return false
	return false
}
