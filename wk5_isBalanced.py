"""
Leetcode 110. Balanced Binary Tree
Easy: Moe feels this one is hard

Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node 
differ in height by no more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree_height(self, root: TreeNode) -> int:
        if root == None:
            return 0
        height = max(self.tree_height(root.left), self.tree_height(root.right)) + 1
        return height
    
    def isBalanced(self, root: TreeNode) -> bool: 
        if root == None:
            return True
        gap = abs(self.tree_height(root.left) - self.tree_height(root.right))    
        return gap <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
      