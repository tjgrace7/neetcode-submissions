class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if five == 0:
                    return False
                ten += 1
                five -=1
            else:
                change = i -5
                if change == 15 and five > 0 and ten > 0:
                    five -=1
                    ten -= 1
                elif change == 15 and five >= 3:
                    five -=3
                else:
                    return False
        return True