"""
Leetcode 101. Symmetric Tree
Easy
Given a binary tree, check whether it is a mirror of itself 
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.isS_Tree(root.left, root.right)
    
    def isS_Tree(self, p: TreeNode, q: TreeNode) -> bool:
        if p != None and q != None:
            return p.val == q.val and self.isS_Tree(p.left, q.right) and self.isS_Tree(p.right, q.left)
        else:
            return p == None and q == None
        