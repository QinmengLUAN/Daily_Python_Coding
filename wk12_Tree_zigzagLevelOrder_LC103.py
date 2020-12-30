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
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res, dq,flag = [], deque(), 1
        dq.append(root)
        
        while dq:
            nx = []
            for _ in range(len(dq)):
                curr_node = dq.popleft()
                nx.append(curr_node.val)
                if curr_node.left:
                    dq.append(curr_node.left)
                if curr_node.right:
                    dq.append(curr_node.right)
            res.append(nx[::flag])
            flag *= -1
        return res
