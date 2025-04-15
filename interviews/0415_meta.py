# We have a game in which consecutive duplicate pieces of the same type cancel each other out and remaining pieces slide in, until no more pieces can be removed.

# Given a board, represented by a string, return the final state of the board after playing the game.

# Input: "abbba"
# Output: "" ("abbba" => "aa" => "")

# Input: "ab"
# Output: "ab"
    
# Input: "abba"
# Output: ""
    
# Input: "aba"
# Output: "aba"

# Stack approach
# add each character to a stack
# if current char matches top of the stack: remove until next char no longer matches top of stack
# return string

def remove_consecutive(input_str):
    stack = []
    for char in input_str:
        if len(stack) > 0:
            prev = stack.pop()
            if cur != prev:
                # abbba
                # [a]
                # 
                stack.append(prev)
                stack.append(char)
            else:
                # remove until nolonger matching, then 
                # while loop
                stack.append(prev)
        else:
            stack.append(char)
            

    return(''.join(stack))


#####
# Given an array of integers, find any one local minimum from the array. A local minimum is defined as an integer in the array that is less than or equal to its neighbors.

# [5, 9, 7, 10, 12] => [5,7]
# 5

# [10, 9, 8, 7, 8]


# Start in the middle
# take steps downhill
# as soon as we find an uphill, return current

#i = 2 val 8

def local_min(input_arr):
    i = len(input_arr)//2
    if input_arr[i] > input_arr[i+1]:
        # walk to the right
        while input_arr[i] > input_arr[i+1]:
            i += 1
            if i > len(input_arr) -1:
                return input_arr[i]
        return input_arr[i]
    if input_arr[i] > input_arr[i-1]:
        # walk to the left
        while input_arr[i] > input_arr[i-1]:
            i -= 1
            if i == 0:
                return input_arr[i]
        return input_arr[i]


