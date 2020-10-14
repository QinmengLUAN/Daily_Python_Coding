"""
Hi, here's your problem today. This problem was recently asked by Facebook:

You are given the root of a binary search tree. Return true if it is a valid binary search tree, and false otherwise. Recall that a binary search tree has the property that all values in the left subtree are less than or equal to the root, and all values in the right subtree are greater than or equal to the root.

Here's a starting point:

class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

def is_bst(root):
  # Fill this in.

a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print is_bst(a)

#    5
#   / \
#  3   7
# / \ /
#1  4 6
"""
class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

def is_bst(root):
    res = []
    self.helper(root, res)
    for i in range(1, len(res)):
        if res[i] <= res[i-1]:
            return False
    return True
        
def helper(self, root, res):
    if root == None:
        return
    self.helper(root.left, res)
    res.append(root.val)
    self.helper(root.right, res)
    return

a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print is_bst(a)
