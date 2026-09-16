class MinStack:

    def __init__(self):
        self.item = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.item.append(val)
        val = min(val,self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.item.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.item[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
