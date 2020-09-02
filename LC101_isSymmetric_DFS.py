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

# Time complexity: O(N)
# Space complexity: O(log(N))
class Solution:
    def isSymmetric_dfs(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.dfs(root.left, root.right)
        
    def dfs(self, nl, nr):
        if nl == nr == None:
            return True
        elif nl == None or nr == None:
            return False
        elif nl.val != nr.val:
            return False
        return self.dfs(nl.left, nr.right) and self.dfs(nl.right, nr.left)
        