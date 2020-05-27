"""
94. Binary Tree Inorder Traversal
Medium: Hash table, Stack, Tree, Iterative
The strategy is very similiar to the first method, the different is using stack.

Time complexity : O(n).
Space complexity : O(n)

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
        res, stack = [], []
        while len(stack) != 0 or root != None:
            while root!= None:
                stack.append(root)
                root = root.left # visit until the left leaf
            if len(stack) == 0:
                return res
            node = stack.pop()
            res.append(node.val)# append  the left leaf until the prvious node, then visit its right dentrite
            root = node.right
        return res