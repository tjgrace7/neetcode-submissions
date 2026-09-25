from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        top = self.rotate()
        self.q.popleft()
        return top

    def top(self) -> int:
        top = self.rotate()
        self.q.append(top)
        self.q.popleft()
        return top

    def empty(self) -> bool:
        if len(self.q)==0: 
            return True
        return False
    def rotate(self) -> int:
        for i in range(len(self.q)-1):
            front = self.q[0]
            self.q.append(front)
            self.q.popleft()
        return self.q[0]

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()