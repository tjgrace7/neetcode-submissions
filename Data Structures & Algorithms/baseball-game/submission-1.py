class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        arr = []
        for op in operations:
            score = 0
            if op == "C":
                total += int(arr[-1]) * -1
                arr.pop()
                continue
            elif op == "D":
                score = int(arr[-1]) * 2
            elif op == "+":
                score = int(arr[-1])+ int(arr[-2])
            else:
                score += int(op)
            total += score
            arr.append(score)
        return total


