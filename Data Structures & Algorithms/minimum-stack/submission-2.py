class MinStack:

    def __init__(self):
        self.stack = []
        self.extraStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.extraStack[-1] if self.extraStack else val)
        self.extraStack.append(val)

    def pop(self) -> None:
        self.extraStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.extraStack[-1]
