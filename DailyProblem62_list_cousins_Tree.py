"""
Hi, here's your problem today. This problem was recently asked by Amazon:

Given a binary tree and a given node value, return all of the node's cousins. Two nodes are considered cousins if they are on the same level of the tree with different parents. You can assume that all nodes will have their own unique value.

Here's some starter code:

class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class Solution(object):
  def list_cousins(self, tree, val):
    # Fill this in.

#     1
#    / \
#   2   3
#  / \   \
# 4   6   5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

print Solution().list_cousins(root, 5)
# [4, 6]
"""
from collections import deque
class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class Solution(object):
  def list_cousins(self, tree, val):
    # Fill this in.
    nodes = {} # key: node.val, value: [level, parent.val]
    pos = None
    dq = deque()
    dq.append((tree, 0)) # curr_layer stores (node, level, parent.val)
    while len(dq) > 0:
        node, level = dq.popleft()
        nodes[node.value] = [level]
        if node.value == val:
            pos = level
        if node.left:
            dq.append((node.left, level+1))
        if node.right:
            dq.append((node.right, level+1))

    if pos == None:
        return []

    res = []
    for k, v in nodes.items():
        if v[0] == pos and k != val:
            res.append(k)
    return res

#     1
#    / \
#   2   3
#  / \   \
# 4   6   5
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.right = Node(3)
root.right.right = Node(5)

print(Solution().list_cousins(root, 5))
# [4, 6]