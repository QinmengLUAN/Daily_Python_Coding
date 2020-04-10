"""
155. Min Stack
Easy: Stack Design

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [[] for i in range(2)]

    def push(self, x: int) -> None:
        if len(self.stack[0]) == 0 or x <= self.stack[1][-1]:
            self.stack[1].append(x)
        else:
            self.stack[1].append(self.stack[1][-1])
        self.stack[0].append(x)

    def pop(self) -> None:
        self.stack[0].pop()
        self.stack[1].pop()
        # print(self.stack)
    def top(self) -> int:
        return self.stack[0][-1]

    def getMin(self) -> int:
        return self.stack[1][-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()