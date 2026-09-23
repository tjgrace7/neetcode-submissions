class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr)-1
        l = arr[i]
        c = 0
        arr[i] = -1
        while i > 0:
            c = arr[i-1]
            arr[i-1] = l
            if c > l: l = c
            c = 0
            i -= 1
        return arr