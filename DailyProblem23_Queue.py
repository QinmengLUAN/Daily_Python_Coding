"""
Hi, here's your problem today. This problem was recently asked by Apple:

Implement a queue class using two stacks. 
A queue is a data structure that supports the FIFO protocol (First in = first out). 
Your class should support the enqueue and dequeue methods like a standard queue.

Here's a starting point:

class Queue:
  def __init__(self):
    # Fill this in.
    
  def enqueue(self, val):
    # Fill this in.

  def dequeue(self):
    # Fill this in.

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print q.dequeue()
print q.dequeue()
print q.dequeue()
# 1 2 3
"""
class Queue:
    def __init__(self):
        self.reversed = False
        self.inStack = []
        self.outStack = []
  
    def enqueue(self, val):
        if self.reversed == True:
            while len(self.outStack) > 0:
                self.inStack.append(self.outStack.pop())
        self.reversed = False
        self.inStack.append(val)
        return

    def dequeue(self):
        if self.reversed == False:
            while len(self.inStack) > 0:
                self.outStack.append(self.inStack.pop())
        self.reversed = True
        return self.outStack.pop()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3