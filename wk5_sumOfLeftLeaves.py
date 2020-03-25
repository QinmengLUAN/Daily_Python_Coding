"""
Leetcoe 404. Sum of Left Leaves
Easy
Binary tree

Find the sum of all left leaves in a given binary tree.
Example:

    3
   / \
  9  20
    /  \
   15   7
There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        total = 0
        if root == None:
            return 0
        if root.left != None and root.left.left == None and root.left.right == None:
            total += root.left.val 
        total = total + self.sumOfLeftLeaves( root.left) +  self.sumOfLeftLeaves(root.right) 
        return total