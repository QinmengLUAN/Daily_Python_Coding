"""
Hi, here's your problem today. This problem was recently asked by Twitter:

Given a tree, find if the binary tree is height balanced or not. A height balanced binary tree is a tree where every node's 2 subtree do not differ in height by more than 1.

Here's some starter code:

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def is_height_balanced(tree):
  # Fill this in.

#     1
#    / \
#   2   3
#  /
# 4  
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)

print(is_height_balanced(n1))
# True

#     1
#    / 
#   2   
#  /
# 4  
n1 = Node(1, n2)
print(is_height_balanced(n1))
# False
"""
# Consider a height-balancing scheme where following conditions should be checked to determine if a binary tree is balanced.
# An empty tree is height-balanced. A non-empty binary tree T is balanced if:
# 1) Left subtree of T is balanced
# 2) Right subtree of T is balanced
# 3) The difference between heights of left subtree and right subtree is not more than 1.
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_height_balanced(tree):
    if not tree:
        return True
    l = dfs(tree.left)
    r = dfs(tree.right)
    if abs(l - r) <= 1 and is_height_balanced(tree.left) and is_height_balanced(tree.right):
        return True
    return False

def dfs(node):
    if not node:
        return 0
    height = max(dfs(node.left), dfs(node.right)) + 1
    return height

#     1
#    / \
#   2   3
#  /
# 4  
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)

print(is_height_balanced(n1))
# True

#     1
#    / 
#   2   
#  /
# 4  
n1 = Node(1, n2)
print(is_height_balanced(n1))
# False
