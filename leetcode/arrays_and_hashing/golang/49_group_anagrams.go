/*
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
*/

// This solution uses a map to store the anagrams. The key is the sorted string and the value is the list of anagrams.
// Time complexity: O(n * klogk) where n is the length of strs and k is the length of the longest string in strs
func groupAnagrams(strs []string) [][]string {
	m := make(map[string][]string)
	for _, str := range strs {
		key := getKey(str)
		m[key] = append(m[key], str)
	}

	res := make([][]string, 0)
	for _, v := range m {
		res = append(res, v)
	}
	return res
}

// Optimized solution
// Time complexity: O(n * k) where n is the length of strs and k is the length of the longest string in strs
func groupAnagrams(strs []string) [][]string {
	// Create a map to store the anagrams
	// The key is an array of 26 integers representing the count of each character in the string
	// The value is the list of anagrams
	m := make(map[[26]int][]string)
	for _, str := range strs {
		// Get the key for the string
		key := getKey(str)
		// Append the string to the list of anagrams
		m[key] = append(m[key], str)
	}

	// Convert map to slice
	res := make([][]string, 0)
	for _, v := range m {
		// Append the list of anagrams to the result
		res = append(res, v)
	}
	return res
}