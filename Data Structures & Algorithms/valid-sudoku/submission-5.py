class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #1 check rows
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                value = board[i][j]
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
        #2 check columns
        for i in range(9):
            seen = set()
            for j in range(9):
                value = board[j][i]
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)
        #3 check squares
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        value = board[r][c]
                        if value == ".":
                            continue
                        if value in seen: 
                            return False
                        seen.add(value)
        return True
