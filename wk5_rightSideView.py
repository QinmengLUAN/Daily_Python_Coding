"""
Leetcode 199. Binary Tree Right Side View
Medium: Breadth-first search (BFS), hard in BTS questions

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        current_layer = []
        if root != None:
            current_layer.append(root)
            
        while len(current_layer) > 0:
            res.append(current_layer[-1].val)
            next_layer = []
            for current_node in current_layer:
                if current_node.left != None:
                    next_layer.append(current_node.left)
                if current_node.right != None:
                    next_layer.append(current_node.right)
            current_layer = next_layer
        return res