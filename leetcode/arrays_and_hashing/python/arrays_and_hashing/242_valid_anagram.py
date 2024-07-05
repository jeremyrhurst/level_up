# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# 
# Example 1:
# 
# Input: s = "anagram", t = "nagaram"
# Output: true
# 
# Example 2:
# 
# Input: s = "rat", t = "car"
# Output: false
# 
# Constraints:
# 
#     1 <= s.length, t.length <= 5 * 104
#     s and t consist of lowercase English letters.

# My own solution using a dictionary to store the frequency of each character in the first string.
# Then iterate over the second string and decrement the frequency of each character in the dictionary.
# If the character is not in the dictionary, return False.
# If the frequency of the character is 1, delete the character from the dictionary.
# If the dictionary is empty (meaning that the solutions match), return True.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
                
        for c in t:
            if c not in freq:
                return False
            elif freq[c] == 1:
                del freq[c]
            else:
                freq[c] -=1
        if not freq:
            return True
        return False
        


# Optimized solution using the Counter class from the collections module.
# The Counter class returns a dictionary with the frequency of each character in the string.
# We can then compare the two dictionaries to see if they are equal.
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


# Optimized solution using the sorted function to sort the strings and compare them.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
