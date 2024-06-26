/*
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
*/

// Encode encodes a list of strings to a single string.
func encode(strs []string) string {
	res := ""
	for _, str := range strs {
		res += strconv.Itoa(len(str)) + "#" + str
	}
	return res
}

// Decode decodes a single string to a list of strings.
func decode(s string) []string {
	res := []string{}
	for i := 0; i < len(s); {
		j := i
		for s[j] != '#' {
			j++
		}
		n, _ := strconv.Atoi(s[i:j])
		res = append(res, s[j+1:j+1+n])
		i = j + 1 + n
	}
	return res
}
