class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        OTL, OTR = 0, len(matrix)-1
        while OTL <= OTR:
            OTM = int((OTL+OTR)/2)
            L, R = 0, len(matrix[OTM])-1
            if matrix[OTM][L] > target:
                OTR = OTM-1
            elif matrix[OTM][R] < target:
                OTL = OTM + 1
            else:
                while L <= R:
                    M = int((L+R)/2)
                    if matrix[OTM][M] < target:
                        L = M + 1
                    elif matrix[OTM][M] > target:
                        R = M-1
                    else: 
                        return True
                break
        return False
    