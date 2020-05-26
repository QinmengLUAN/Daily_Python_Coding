'''
232. Implement Queue using Stacks
Easy: Stack & Design, 2 stacks, O(1) space, O(1) time complexity

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
'''
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.reversed = False
        self.inStack = []
        self.outStack = []
    
    def reverse_func(self):
        if self.reversed == False:
            while len(self.inStack) != 0:
                self.outStack.append(self.inStack.pop())
            self.reversed = True     
        else:
            while len(self.outStack) != 0:
                self.inStack.append(self.outStack.pop()) 
            self.reversed = False
    
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.reversed == True:
            self.reverse_func()
        self.inStack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.reversed == False:
            self.reverse_func()
        return self.outStack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.reversed == False:
            self.reverse_func()
        if len(self.outStack) != 0:    
            return self.outStack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.inStack) == 0 and len(self.outStack) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()