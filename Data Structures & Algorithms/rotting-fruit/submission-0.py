class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        while fresh > 0 and q:

            for i in range(len(q)):
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1):
                        fresh -=1
                        q.append((row, col))
                        grid[row][col] = 2
            time +=1
        return time if fresh == 0 else -1

