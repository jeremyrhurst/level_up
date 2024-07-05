# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
# and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def check(self, s: str, begin: int, end: int) -> bool:
        # If the begin pointer is not character, recur +1 begin
        # if the end pointer is not a character, recur -1 end
        # else if lower case of begin and end doesn't match return false
        # recur +1 begin -1 end
        if begin >= end:
            return(True)
        if s[begin].isalpha() == False:
            return self.check(s, begin + 1, end)
        elif s[end].isalpha() == False:
            return self.check(s, begin, end-1)
        else:
            b = s[begin].lower()
            e = s[end].lower()
            if b != e:
                return False
            return self.check(s, begin + 1, end -1)


    def isPalindrome(self, s: str) -> bool:
        # Recursively check if begin and end pointer are the same
        # if not return false
        return self.check(s, 0, len(s)-1)

