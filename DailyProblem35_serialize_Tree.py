"""
Hard, Tree
Hi, here's your problem today. This problem was recently asked by Apple:

You are given the root of a binary tree. You need to implement 2 functions:

1. serialize(root) which serializes the tree into a string representation
2. deserialize(s) which deserializes the string back to the original tree that it represents

For this problem, often you will be asked to design your own serialization format. However, for simplicity, let's use the pre-order traversal of the tree. Here's your starting point:

"""
class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    # pre-order printing of the tree.
    result = ''
    result += str(self.val)
    if self.left:
      result += str(self.left)
    if self.right:
      result += str(self.right)
    return result

def serialize(root):
  # Fill this in.
  data = []
  serialize_helper(root, data)
  return data

def serialize_helper(node, data):
  if node == None:
    data.append("#")
  else:
    data.append(node.val)
    serialize_helper(node.left, data)
    serialize_helper(node.right, data)
  return 

def deserialize(data):
  # Fill this in.
  data = data.split()
  if len(data) == 0 or data[0] == "#":
    return None
  rt, _ = deserialize_helper(data, 0)
  return rt

# return (rootNode, nextIndex)
def deserialize_helper(data, idx):
  if idx >= len(data):
    return None, idx
  if data[idx] == "#":
    return None, idx+1
  rt = Node(data[idx])
  rt.left, idx = deserialize_helper(data, idx+1)
  rt.right, idx = deserialize_helper(data, idx)
  return rt, idx
########################################################
# Test
#     1
#    / \
#   3   4
#  / \   \
# 2   5   7
tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)

print(serialize(tree))
# 1 3 2 # # 5 # # 4 # 7 # #
print(deserialize('1 3 2 # # 5 # # 4 # 7 # #'))
# 132547