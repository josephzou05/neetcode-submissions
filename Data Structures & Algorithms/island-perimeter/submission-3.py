class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    #below
                    result += (r + 1 >= rows or grid[r + 1][c] == 0)
                    #right
                    result += (c + 1 >= cols or grid[r][c + 1] == 0)
                    #above
                    result += (r - 1 < 0 or grid[r - 1][c] == 0)
                    #left
                    result += (c - 1 < 0 or grid[r][c - 1] == 0)
        return result