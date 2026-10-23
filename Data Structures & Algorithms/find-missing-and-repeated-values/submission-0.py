class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        counts = {n: 0 for n in range(1, len(grid) * len(grid)+1)}
        arr = [0, 0]
        
        for i in range(0, len(grid) ):
            for j in range(0, len(grid)):
                counts[grid[i][j]] +=1
        print(counts)
        for key, val in counts.items():
            if val == 2:
                arr[0] =key
            if val == 0:
                arr[1] = key
        return arr