class MinStack:

    def __init__(self):
        self.value = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.value.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.value:
            pop_val = self.value.pop()
            if self.min_stack[-1] == pop_val:
                self.min_stack.pop()

    def top(self) -> int:
        if self.value:
            return self.value[-1]

    def getMin(self) -> int:
        return self.min_stack[-1] 



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
val = 10
obj.push(val)
# obj.pop()
print(obj.getMin())
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
