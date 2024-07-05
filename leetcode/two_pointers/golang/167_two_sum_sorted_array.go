/*
167. Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
*/

package main

/*
 Set a pointer for beginning and end
 if sum equals target return first, last
 if sum is greater than target, decrease last
 if sum is less than target, increase first
*/

func twoSum(numbers []int, target int) []int {
	first := 0
	last := len(numbers) - 1
	for first < last {
		sum := numbers[first] + numbers[last]
		if sum == target {
			return []int{first + 1, last + 1}
		} else if sum > target {
			last--
		} else {
			first++
		}
	}
	return nil
}
