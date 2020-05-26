'''
716: Max Stack
Easy: Stack, Design, OOD
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
'''
class MaxStack():
    def __init__(self):
        self.lis = []
        self.currM = []

    def push(self, x):
        self.lis.append(x)
        if len(self.currM) == 0:
            self.currM.append(x)
        else:
            self.currM.append(max(x, self.currM[-1]))
        return
    def pop(self):
        val = self.lis.pop()
        self.currM.pop()
        return val

    def top(self):
        if len(self.lis) == 0:
            return None
        else:
            return self.lis[-1]

    def peekMax(self):
        if len(self.currM) == 0:
            return None
        else:
            return self.currM[-1]

    def popMax(self):
        maxValue = self.currM[-1]
        poppedVal = []
        val = self.pop()
        while val != maxValue:
            poppedVal.append(val)
            val = self.pop()
        for item in poppedVal[::-1]:
            self.push(item)
        return maxValue

stack = MaxStack()
stack.push(5); 
stack.push(1);
stack.push(5);
print(stack.top())
print(stack.popMax())
print(stack.top())
print(stack.peekMax())
print(stack.pop())
print(stack.top())
                                                          

