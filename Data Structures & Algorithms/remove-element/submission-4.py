class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)-1
        k = 0
        if len(nums) == 0:
            return k
        while nums[j] == val:
            nums[j] = -1
            j -= 1
            k +=1
        while i <= j:
            if nums[j] == val:
                nums[j] = -1
                j -= 1
                k +=1
            if nums[i] == val:
                tmp = nums[j]
                nums[j] = -1
                nums[i] = tmp
                j -= 1
                k +=1
            i +=1
        print(nums)
        return len(nums)-k

        