"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Implement a class for a stack that supports all the regular functions (push, pop) and an additional function of max() which returns the maximum element in the stack (return None if the stack is empty). Each method should run in constant time.

class MaxStack:
  def __init__(self):
    # Fill this in.

  def push(self, val):
    # Fill this in.

  def pop(self):
    # Fill this in.

  def max(self):
    # Fill this in.

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print s.max()
# 3
s.pop()
s.pop()
print s.max()
# 2
"""
class MaxStack:
  def __init__(self):
    # Fill this in.
    self.stack = []
    self.max_val = []

  def push(self, val):
    # Fill this in.
    if len(self.max_val) == 0:
      self.max_val.append(val)
    else:
      self.max_val.append(max(val, self.max_val[-1]))
    self.stack.append(val)

  def pop(self):
    # Fill this in.
    self.stack.pop()
    self.max_val.pop()

  def max(self):
    # Fill this in.
    return self.max_val[-1]


s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2