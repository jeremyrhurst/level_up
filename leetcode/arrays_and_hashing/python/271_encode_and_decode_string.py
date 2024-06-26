# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
 
class Solution:

    def encode(self, strs: List[str]) -> str:
        return '|'.join(strs)

    def decode(self, s: str) -> List[str]:
        ans = []
        prev = 0
        for i in range(len(s)):
            if s[i] == '|':
                ans.append(s[prev:i])
                prev = i+1
        ans.append(s[prev:])


        return ans