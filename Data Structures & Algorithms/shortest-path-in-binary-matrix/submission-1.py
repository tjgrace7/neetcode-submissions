class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        quene = deque()
        visit = set()
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        quene.append((0,0))
        ROWS, COLS = len(grid), len(grid[0])

        visit.add((0, 0))
        length = 1
        if grid[0][0]== 1 or grid[len(grid)-1][len(grid[0])-1] == 1:
            return -1
        while quene:
            for i in range(len(quene)):
                r, c = quene.popleft()
                if r == ROWS -1 and c == COLS -1:
                    return length
                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or 
                        r + dr == ROWS or c + dc == ROWS or 
                        (r + dr, c + dc) in visit or grid[r+dr][c+dc] == 1):
                        continue
                    quene.append((r+dr, c + dc))
                    visit.add((r + dr, c + dc)) 
            length += 1

        if (len(grid)-1, len(grid[0])-1) not in visit:
            return -1
        return length