class MinStack:

    def __init__(self):
        self.stack = []
        self.extraStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.extraStack) == 0:
            self.extraStack.append(val)
        else:
            if val <= self.extraStack[-1]:
                self.extraStack.append(val)

    def pop(self) -> None:
        if self.extraStack[-1] == self.stack[-1]:
            self.extraStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.extraStack[-1]
