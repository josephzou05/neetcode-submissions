class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        time = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for drow, dcol in directions:
                    row, col = r + drow, c + dcol
                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col] == 1):
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1
            time += 1
        if fresh == 0:
            return time
        return -1