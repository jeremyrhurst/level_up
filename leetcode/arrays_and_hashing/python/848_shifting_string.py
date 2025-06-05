
'''
You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

    For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.

 

Example 1:

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.

Example 2:

Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"

 

Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.
    shifts.length == s.length
    0 <= shifts[i] <= 109


'''

# My own solution: fails for large inputs
# time complexity: O(n^2) because of the nested loops

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans = []
        for char in s:
            ans.append(ord(char)-ord('a'))
        
        for i in range(len(shifts)):
            for j in range(i+1):
                q, r = divmod(shifts[i], 26)
                ans[j] += r
                z = ord('z') - ord('a')
                if ans[j] > z:
                    ans[j] -= z+1

        for i in range(len(ans)):
            ans[i] = chr(ans[i]+ord('a'))
        return ''.join(ans)

# Optimized solution using cumulative shifts
# This solution has a time complexity of O(n) because it processes the shifts in a single pass from the end of the list to the beginning.
# Optimized solution iterating backwards through the shifts array and applying cumulative shifts to the characters in the string.
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        cumulative_shift = 0
        for i in range(len(shifts) - 1, -1, -1):
            cumulative_shift += shifts[i]
            cumulative_shift %= 26
            ans[i] += cumulative_shift
            z = ord('z') - ord('a')
            if ans[i] > z:
                ans[i] -= z + 1
        for i in range(len(ans)):
            ans[i] = chr(ans[i] + ord('a'))
        return ''.join(ans)
            

