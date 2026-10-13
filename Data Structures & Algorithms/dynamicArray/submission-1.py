class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if self.arr[i] == 0:
            self.size +=1
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.set(self.size, n)


    def popback(self) -> int:
        back = self.arr[self.size-1] 
        self.arr[self.size-1] = 0
        self.size -=1
        return back

    def resize(self) -> None:
        arr = self.arr
        self.capacity *= 2
        self.arr = [0] *self.capacity
        for i in range(len(arr)):
            if arr[i] != 0:
                self.arr[i] = arr[i]


    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity