class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def Euclidean(num):
            return (num[0]**2+num[1]**2)**0.5
        
        def quickSort(s, e):
            if e-s+1 <= 1:
                return
            left = s
            pivot = points[e]
            for i in range(s, e):
                if Euclidean(points[i]) < Euclidean(pivot):
                    tmp = points[left]
                    points[left] = points[i]
                    points[i] = tmp
                    left += 1
            print(points[e], points[left])
            points[e] = points[left]
            points[left] = pivot
            quickSort(s, left-1)
            quickSort(left+1, e)
        quickSort(0, len(points)-1)
        return points[0:k]