import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(p):
            return p[0]**2+p[1]**2
        def partition(l, r):
            pivot = dist(points[r])
            left = l
            for i in range(l, r):
                if dist(points[i]) < pivot:
                    points[left], points[i] = points[i], points[left]
                    left +=1
            points[left], points[r] = points[r], points[left]
            return left
        l, r = 0, len(points)-1
        while l <= r:
            p = partition(l,r)
            if p == k:
                break
            elif p < k:
                l = p +1
            else:
                r = p-1
        return points[:k] 
        