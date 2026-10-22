class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        s = 0
        e = len(names)-1
        def quickSort(s, e, arr, arr2):
            if e-s+1 <=1:
                return arr
            pivot = arr[e]
            pivot2 = arr2[e]

            left = s

            for i in range(s,e):
                if arr[i] > pivot:
                    tmp2 = arr2[left]
                    tmp = arr[left]
                    arr[left] = arr[i]
                    arr2[left] = arr2[i]
                    arr[i] = tmp
                    arr2[i] = tmp2
                    left +=1
            arr[e] = arr[left]
            arr2[e] = arr2[left]
            arr[left] = pivot
            arr2[left] = pivot2
            quickSort(s, left-1, arr, arr2)
            quickSort(left +1, e, arr, arr2)
            return arr2
        return quickSort(s,e, heights, names)
                