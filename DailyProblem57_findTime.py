"""
Hi, here's your problem today. This problem was recently asked by AirBNB:

We have a list of tasks to perform, with a cooldown period. We can do multiple of these at the same time, but we cannot run the same task simultaneously.

Given a list of tasks, find how long it will take to complete the tasks in the order they are input.
tasks = [1, 1, 2, 1]
cooldown = 2
output: 7 (order is 1 _ _ 1 2 _ 1)
def findTime(arr, cooldown):
  # Fill this in.

print findTime([1, 1, 2, 1], 2)
# 7
"""
import collections
def findTime(arr, cooldown):
    c = collections.Counter(arr)
    max_count = max(c.values())
    return (max_count-1) * cooldown + max_count

print(findTime([1, 1, 2, 1], 2))
# 7
print(findTime([1, 1, 1], 2))
# 7
print(findTime([1, 2, 3], 2))
# 4