/*
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false



Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.
*/

// Time: O(n)
// Space: O(n)
// Hash Table Solution
package main

import "sort"

func isAnagram(s string, t string) bool {
	// If the length of the strings is different, return false
	if len(s) != len(t) {
		return false
	}
	// Create a map to store the characters
	// The key is the character and the value is the count of the character
	m := make(map[rune]int)
	// Iterate through the characters of the first string
	for _, c := range s {
		// Increment the count of the character in the map
		m[c]++
	}
	// Iterate through the characters of the second string
	for _, c := range t {
		// Decrement the count of the character in the map
		m[c]--
		// If the count of the character is less than 0, return false
		if m[c] < 0 {
			return false
		}
	}
	// If all the characters have the same count, return true
	return true
}

// Time: O(n)
// Space: O(1)
// Array Solution
func isAnagram(s string, t string) bool {
	// If the length of the strings is different, return false
	if len(s) != len(t) {
		return false
	}
	// Create an array to store the count of characters
	// Initialize the array with 26 zeros
	count := [26]int{}
	// Iterate through the characters of the first string
	for _, c := range s {
		// Increment the count of the character in the array
		count[c-'a']++
	}
	// Iterate through the characters of the second string
	for _, c := range t {
		// Decrement the count of the character in the array
		count[c-'a']--
		// If the count of the character is less than 0, return false
		if count[c-'a'] < 0 {
			return false
		}
	}
	// If all the characters have the same count, return true
	return true
}

// Time: O(n)
// Space: O(n)
// Sort Solution
func isAnagram(s string, t string) bool {
	// If the length of the strings is different, return false
	if len(s) != len(t) {
		return false
	}
	// Convert the strings to slices of bytes
	s1 := []byte(s)
	t1 := []byte(t)
	// Sort the slices of bytes
	sort.Slice(s1, func(i, j int) bool { return s1[i] < s1[j] })
	sort.Slice(t1, func(i, j int) bool { return t1[i] < t1[j] })
	// Convert the sorted slices of bytes back to strings
	s = string(s1)
	t = string(t1)
	// If the sorted strings are equal, return true
	return s == t
}
