"""
94. Binary Tree Inorder Traversal
Medium: Hash table, Stack, Tree, Recursion

Time complexity : O(n). The time complexity is O(n) because the recursive function is T(n) = 2⋅T(n/2)+1.
Space complexity : The worst case space required is O(n), and in the average case it's O(log n)O(logn) where n is number of nodes.

Given a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        lis = []
        self.helper(root, lis)
        return lis
    def helper(self, root, lis):
        if root != None:
            self.helper(root.left,lis)
            lis.append(root.val)
            self.helper(root.right,lis)