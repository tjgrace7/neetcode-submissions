class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ogcolor = image[sr][sc]
        def dfs(r, c, visit) -> List[List[int]]:
            ROWS, COLS = len(image), len(image[0])
            if (min(r,c) < 0 or r == ROWS or c == COLS or image[r][c] != ogcolor or (r, c) in visit):
                return image
            image[r][c] = color
            visit.add((r, c))
            dfs(r +1, c, visit)
            dfs(r-1, c, visit)
            dfs(r, c + 1, visit)
            dfs(r, c -1, visit)
            visit.remove((r, c))
            return image
        return dfs(sr, sc, set(()))

            