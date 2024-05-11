# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# 
# Example 1:
# 
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


# My solution by sorting each string and using that as the key in a dictionary.
# Time complexity: O(n*mlogm) where n is the number of strings and m is the length of the longest string.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for string in strs:
            s_str = ''.join(sorted(string))
            if s_str in ans:
                ans[s_str].append(string)
            else:
                ans[s_str] = [string]
        return ans.values()

# Time optimized solution using count array and ord function to get the frequency of each character in the string.
# Time complexity: O(n*m) where n is the number of strings and m is the length of the longest string.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for string in strs:
            count = [0]*26
            for c in string:
                # Subtracting the ASCII value of 'a' to get the index of the character in the count array.
                count[ord(c) - ord('a')] += 1
            s_str = tuple(count)
            if s_str in ans:
                ans[s_str].append(string)
            else:
                ans[s_str] = [string]
        return ans.values()