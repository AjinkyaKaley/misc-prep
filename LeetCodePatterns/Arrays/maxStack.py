class MaxStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        m = x
        if self.stack and self.stack[-1][1] > x:
            m = self.stack[-1][1]

        self.stack.append((x, m))

    def pop(self):
        return self.stack.pop()[0]

    def top(self):
        return self.stack[-1][0]

    def peekMax(self):
        return self.stack[-1][1]

    def popMax(self):
        m = self.stack[-1][1]
        b = []
        while self.stack[-1][0] != m:
            b.append(self.stack.pop()[0])

        self.pop()
        for _b in reversed(b):
            self.push(_b)
        return m

sln = MaxStack()
sln.push(5)
sln.push(1)
sln.popMax()
sln.peekMax()
