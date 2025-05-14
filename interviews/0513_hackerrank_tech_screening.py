# https://leetcode.com/problems/special-binary-string/description/
# Given a binary string, find the largest magical binary string that can be formed by removing some characters from the original string.O
def largestMagical(binString):
   
   
    # Write your code here
    #1101 1100 00
    # 1: has to start with 1s
    # 2: the number of 0s has to be equal to or less than the number of 1s
    
    #1 1100 10 0
    # 1 10 1100 0
    # 
    # 11100100
    #11100100
    # 1 identify substrings
    # determine order of substrings
    # return answer
    
    # stack solution for finding good binary strings:
    # find good binary strings until end of binary strings
    # sort that temp list and add to solution

    
    cur = []
    ans = []
    ones = 0
    last_zero = False
    print(binString)
    for char in binString:
        if char == '1':
            ones += 1
            if last_zero:
                ans.append(''.join(cur))
                cur = []
                ones = 1
            last_zero = False
        else:
            last_zero = True
            if ones > 0:
                ones -= 1
                cur.append('0')
                cur.insert(0, '1')
    ans.append(''.join(cur))
    print(ans)
    # continue adding to ans where there are good strings
    # As soon as good strings end, sort ans with strings that start with most 1s first
    # join all ans strings together, append to final ans
    # Also add to the result if not a good string
    return('')