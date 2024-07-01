/*
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
*/

func isValidSudoku(board [][]byte) bool {
	primes := []int{2, 3, 5, 7, 11, 13, 17, 19, 23}

	rows := make(map[int]int)
	cols := make(map[int]int)

	squares := make([][]int, 3)
	squares[0] = []int{1, 1, 1}
	squares[1] = []int{1, 1, 1}
	squares[2] = []int{1, 1, 1}

	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {

			if board[i][j] != '.' {

				boardPosition, _ := strconv.Atoi(string(board[i][j]))

				if rows[boardPosition] == 0 {
					rows[boardPosition] = 1
				}
				if cols[boardPosition] == 0 {
					cols[boardPosition] = 1
				}

				if rows[boardPosition]%primes[i] == 0 ||
					cols[boardPosition]%primes[j] == 0 ||
					squares[i/3][j/3]%primes[boardPosition-1] == 0 {
					return false
				}

				cols[boardPosition] *= primes[j]
				rows[boardPosition] *= primes[i]
				squares[i/3][j/3] *= primes[boardPosition-1]
			}
		}
	}
	return true
}