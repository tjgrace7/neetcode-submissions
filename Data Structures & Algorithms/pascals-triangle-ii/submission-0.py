class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        COLS = 1
        ROWS = rowIndex + 1
        res = [[0] * ROWS for _ in range(ROWS)]
        i = 0
        while i < ROWS:
            for j in range(COLS):
                if j == 0 or j == COLS - 1:
                    res[i][j] = 1
                elif j - 1 >= 0:

                    res[i][j] = res[i-1][j]+res[i-1][j-1]
            COLS +=1
            i +=1
        return res[rowIndex]
