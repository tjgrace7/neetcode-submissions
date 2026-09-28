class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for num in nums2:
            nums1[m] = num
            m += 1
        s = 0
        e = m-1
        nums1 = self.mergeSort(nums1,s, e)
    def mergeSort(self, nums: List[int], s: int, e: int) -> List[int]:
        if(e-s+1 <= 1):
            return nums
        
        m =int((e+s)/2)
        self.mergeSort(nums, s, m)
        self.mergeSort(nums, m+1, e)
        self.mesh(nums, s, m, e)
        return nums
    def mesh(self, arr, s, m, e):
        L = arr[s: m+1]
        R = arr[m+1: e +1]

        i = 0 #index for left
        j = 0 # index for right
        k = s # Index for arr

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else: 
                arr[k] = R[j]
                j += 1
            k +=1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k +=1
        


        

        