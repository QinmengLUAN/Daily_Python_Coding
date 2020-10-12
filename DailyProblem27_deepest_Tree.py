"""
Hi, here's your problem today. This problem was recently asked by Google:

You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

Example:

    a
   / \
  b   c
 /
d

The deepest node in this tree is d at depth 3.

Here's a starting point:

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    # string representation
    return self.val


def deepest(node):
  # Fill this in.

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print deepest(root)
# (d, 3)
"""

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    # string representation
    return self.val


def deepest(node):
  level = 0
  return dfs(node, None, level)


def dfs(node, val, level):
  if node == None:
    return (val, level)
  else:
    level += 1
    val = node.val
    l_val, l_level = dfs(node.left, val, level)
    r_val, r_level = dfs(node.right, val, level)
    if l_level > r_level:
      return (l_val, l_level)
    else:
      return (r_val, r_level)


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))
# (d, 3)