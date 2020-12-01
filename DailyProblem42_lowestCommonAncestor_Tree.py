"""
Hi, here's your problem today. This problem was recently asked by Apple:

You are given the root of a binary tree, along with two nodes, A and B. Find and return the lowest common ancestor of A and B. For this problem, you can assume that each node also has a pointer to its parent, along with its left and right child.

class TreeNode:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.parent = None
    self.val = val


def lowestCommonAncestor(root, a, b):
  # Fill this in.

#   a
#  / \
# b   c
#    / \
#   d*  e*
root = TreeNode('a')
root.left = TreeNode('b')
root.left.parent = root
root.right = TreeNode('c')
root.right.parent = root
a = root.right.left = TreeNode('d')
root.right.left.parent = root.right
b = root.right.right = TreeNode('e')
root.right.right.parent = root.right

print lowestCommonAncestor(root, a, b).val
# c
"""

class TreeNode:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.parent = None
    self.val = val


def lowestCommonAncestor(root, a, b):
    # Fill this in. Recursion to find a and b, return the root
    # If both a 和 b exist，return  LCA
    # If only a exists，return a
    # If only b exists，return b
    # If neither a or b exists，return  LCA

    if root == None:
        return None
        
    if root == a or root == b:
        return root

    left_result = lowestCommonAncestor(root.left, a, b)
    right_result = lowestCommonAncestor(root.right, a, b)

    # A 和 B 一边一个
    if left_result and right_result: 
        return root
    
    # 左子树有一个点或者左子树有LCA
    if left_result:
        return left_result
    
    # 右子树有一个点或者右子树有LCA
    if right_result:
        return right_result
    
    # 左右子树啥都没有
    return None

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#   a
#  / \
# b   c
#    / \
#   d*  e*
root = TreeNode('a')
root.left = TreeNode('b')
root.left.parent = root
root.right = TreeNode('c')
root.right.parent = root
a = root.right.left = TreeNode('d')
root.right.left.parent = root.right
b = root.right.right = TreeNode('e')
root.right.right.parent = root.right

print(lowestCommonAncestor(root, a, b).val)