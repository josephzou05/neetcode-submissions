class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #1) check if rows are valid
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])

        #2) check if columns are valid
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                if board[j][i] != ".":
                    if board[j][i] in seen:
                        return False
                    seen.add(board[j][i])
        #3) check if squares are valid
        for box_row in range(0, 9, 3): #0, 3, 6
            for box_column in range(0, 9, 3): #0, 3, 6
                seen = set()
                for i in range(box_row, box_row + 3):
                    for j in range(box_column, box_column + 3):
                        if board[i][j] != ".":
                            if board[i][j] in seen:
                                return False
                            seen.add(board[i][j])
        return True



