'''
Decode Ways

A string consisting of uppercase english characters can be encoded to a number using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping above. There may be multiple ways to decode a message. For example, "1012" can be mapped into:

    "JAB" with the grouping (10 1 2)
    "JL" with the grouping (10 12)

The grouping (1 01 2) is invalid because 01 cannot be mapped into a letter since it contains a leading zero.

Given a string s containing only digits, return the number of ways to decode it. You can assume that the answer fits in a 32-bit integer.

Example 1:

Input: s = "12"

Output: 2

Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "01"

Output: 0

Explanation: "01" cannot be decoded because "01" cannot be mapped into a letter.

Constraints:

    1 <= s.length <= 100
    s consists of digits
'''


# https://leetcode.com/problems/decode-ways/description/
# Dynamic Programming Top Down technique
# Space complexity: O(n)
# time complexity: O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            res = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
                res += dfs(i + 2)
            # Cache the result
            dp[i] = res
            return res
        return dfs(0)

# Dynamic Programming Bottom Up technique
# Space complexity: O(n)
# time complexity: O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        dp[n - 1] = 1 if s[n - 1] != '0' else 0
        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                continue
            dp[i] = dp[i + 1]
            if s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6'):
                dp[i] += dp[i + 2]
        return dp[0]

# Dynamic Programming Bottom Up technique with space optimization
# This approach uses only O(1) space instead of O(n) space
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp1, dp2 = 1, 1 if s[n - 1] != '0' else 0
        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                dp1, dp2 = dp2, 0
                continue
            temp = dp1
            dp1 = dp2
            if s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6'):
                dp2 += temp
            else:
                dp2 = temp
        return dp1
