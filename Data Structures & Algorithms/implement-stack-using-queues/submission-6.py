class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        val = 0
        end = len(self.q)-1
        for i in range(len(self.q)):
            val = self.q.popleft()
            if i != end:
                self.q.append(val)
        return val
            

    def top(self) -> int:
        val = 0
        for i in range(len(self.q)):
            val = self.q.popleft()
            self.q.append(val)
        return val
        

    def empty(self) -> bool:
        if len(self.q) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()