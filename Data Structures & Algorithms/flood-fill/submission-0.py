class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ogcolor = image[sr][sc]
        def dfs(grid, r, c, visit) -> List[List[int]]:
            ROWS, COLS = len(grid), len(grid[0])
            if (min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] != ogcolor or (r, c) in visit):
                return grid
            grid[r][c] = color
            visit.add((r, c))
            dfs(grid, r +1, c, visit)
            dfs(grid, r-1, c, visit)
            dfs(grid, r, c + 1, visit)
            dfs(grid, r, c -1, visit)
            visit.remove((r, c))
            return grid
        return dfs(image, sr, sc, set(()))

            