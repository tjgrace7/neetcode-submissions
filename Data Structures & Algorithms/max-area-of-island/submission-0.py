class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c) -> int:
            if (min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            islcount = 1
            islcount += dfs(r+1, c)
            islcount += dfs(r-1, c)
            islcount += dfs(r, c +1)
            islcount += dfs(r, c-1)
            return islcount
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count = dfs(r, c)
                    if count > area:
                        area = count
        return area