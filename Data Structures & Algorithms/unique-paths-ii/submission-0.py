class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        def dfs(r, c, cache) -> int:
            if r == ROWS or c == COLS or obstacleGrid[r][c] ==1:
                return 0
            if  cache[r][c] != -1:
                return cache[r][c]
            if r == ROWS-1 and c == COLS-1:
                return 1
            cache[r][c] = dfs(r+1, c, cache) + dfs(r, c +1, cache)
            return cache[r][c]
        return dfs(0, 0, [[-1] * len(obstacleGrid[0]) for i in range(len(obstacleGrid))])