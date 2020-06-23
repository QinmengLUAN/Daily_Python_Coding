"""
103. Binary Tree Zigzag Level Order Traversal
Medium:Tree, BFS, DFS

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
# Solution 2: DFS
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.helper(root, 0, res)
        return res
    
    def helper(self, root, layer, res):
        if root == None:
            return
        if layer >= len(res):
            res.append([])
        if layer % 2 == 0:
            res[layer].append(root.val)
        else:
            res[layer].insert(0, root.val)
        self.helper(root.left, layer + 1, res)
        self.helper(root.right, layer + 1, res)
    
# Solution 1: BFS
    def zigzagLevelOrder1(self, root: TreeNode) -> List[List[int]]:
        deq, res = deque(), []
        if root != None:
            deq.append(root)
            
        idx_layer = 0
        while len(deq) > 0:
            curr_res = []
            idx_layer += 1
            for i in range(len(deq)):
                curr_node = deq.popleft()
                curr_res.append(curr_node.val)
                
                if curr_node.left != None:
                    deq.append(curr_node.left)
                if curr_node.right != None:
                    deq.append(curr_node.right)
                    
            if idx_layer % 2 == 1:        
                res.append(curr_res)
            else:
                curr_res.reverse()
                res.append(curr_res)
                
        return res