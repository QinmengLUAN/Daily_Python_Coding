"""
Leetcode107. Binary Tree Level Order Traversal II
Easy: Breadth-first search (BFS), hard in BTS questions

Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).
For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        current_layer = []
        res = []
        if root != None:
            current_layer.append(root)  
        while len(current_layer) > 0:
            res.append([curr_layer_node.val for curr_layer_node in current_layer])   
            
            next_layer = []
            for current_node in current_layer:
                if current_node.left != None:
                    next_layer.append(current_node.left)
                if current_node.right != None:
                    next_layer.append(current_node.right)             
            current_layer = next_layer
            
        return reversed(res)