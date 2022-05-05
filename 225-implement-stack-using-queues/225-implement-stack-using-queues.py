class MyStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, x: int) -> None:
        self.stack=[x]+self.stack
        

    def pop(self) -> int:
        op=self.stack[0]
        self.stack=self.stack[1:]
        return op
        

    def top(self) -> int:
        op=self.stack[0]
        return op

    def empty(self) -> bool:
        return len(self.stack)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()