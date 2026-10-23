class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        mat = [[0] * ROWS for _ in range(COLS)]
        c = 0
        while c < COLS:
            r = 0
            while r < ROWS:
                mat[c][r] = matrix[r][c]
                r +=1
            c +=1
        return mat