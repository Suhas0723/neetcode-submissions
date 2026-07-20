class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def helper(i, row, col):
            if i == len(word):
                return True
            if (
                not (0 <= row < ROWS)
                or not (0 <= col < COLS)
                or board[row][col] != word[i]
                or board[row][col] == "#"
            ):
                return False

            board[row][col] = "#"


            res = helper(i + 1, row + 1, col) or helper(i + 1, row - 1, col) or helper(i + 1, row, col + 1) or helper(i + 1, row, col - 1)

            board[row][col] = word[i]

            return res

        
        for r in range(ROWS):
            for c in range(COLS):
                if helper(0, r, c):
                    return True

        return False
