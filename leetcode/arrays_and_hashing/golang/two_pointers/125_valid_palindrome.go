/*
Is Palindrome

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true

Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false

Explanation: "tabacat" is not a palindrome.

Constraints:

    1 <= s.length <= 1000
    s is made up of only printable ASCII characters.

*/

// Time: O(n)
// Space: O(1)
// Two Pointers Solution
package main

import "strings"

func isPalindrome(s string) bool {
	// Convert the string to lowercase
	s = strings.ToLower(s)
	// Initialize the left and right pointers
	left, right := 0, len(s)-1
	// Iterate until the left pointer is less than the right pointer
	for left < right {
		// If the characters at the left and right pointers are not alphanumeric, move the pointers
		if !isAlphanumeric(s[left]) {
			left++
		} else if !isAlphanumeric(s[right]) {
			right--
		} else {
			// If the characters at the left and right pointers are alphanumeric, check if they are equal
			if s[left] != s[right] {
				return false
			}
			// Move the pointers
			left++
			right--
		}
	}
	// If the string is a palindrome, return true
	return true
}

func isAlphanumeric(b byte) bool {
	return (b >= 'a' && b <= 'z') || (b >= 'A' && b <= 'Z') || (b >= '0' && b <= '9')
}
