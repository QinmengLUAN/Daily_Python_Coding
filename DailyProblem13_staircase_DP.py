"""
Hi, here's your problem today. This problem was recently asked by LinkedIn:

You are given a positive integer N which represents the number of steps in a staircase. 
You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.

def staircase(n):
  # Fill this in.
  
print staircase(4)
# 5
print staircase(5)
# 8

Can you find a solution in O(n) time?
"""
def staircase(n):
  # Fill this in.
  f = [0] * n
  f[0] = 1
  f[1] = 2
  for i in range(2, n):
    f[i] = f[i - 1] + f[i - 2]
  return f[-1]
  
print(staircase(4))
# 5
print(staircase(5))
# 8