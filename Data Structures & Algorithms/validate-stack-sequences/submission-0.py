class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        res = []
        pop = 0
        for i in range(len(pushed)):
            res.append(pushed[i])

            while len(res) > 0 and res[len(res)-1] == popped[pop]:
                res.pop()
                pop +=1   
        if pop < len(popped)-1:
            return False
        return True
