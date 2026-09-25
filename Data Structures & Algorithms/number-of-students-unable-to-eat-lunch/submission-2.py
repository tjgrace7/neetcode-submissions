class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circ = students.count(0)
        square = len(students)-circ
        for s in sandwiches:
            if s == 0:
                if circ == 0:
                    return square
                circ -= 1
            else:
                if square == 0:
                    return circ
                square -= 1
        return 0