"""
102. Binary Tree Level Order Traversal
Medium: Tree, DFS, BFS

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Method 1: DFS
* Use a variable to track level in the tree and use simple Pre-Order traversal
* Add sub-lists to result as we move down the levels
* Time Complexity: O(N)
* Space Complexity: O(N) + O(h) for stack space
"""
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
    # DFS
        res = []
        self.helper(root, 0, res)
        return res
    
    def helper(self, root, level, res): 
        if root == None:
            return
        if len(res) <= level:
            res.append([])
        res[level].append(root.val)
        self.helper(root.left, level + 1, res)
        self.helper(root.right, level + 1, res)

"""
Method 2: BFS
* Using BFS, at any instant only L1 and L1+1 nodes are in the queue.
* When we start the while loop, we have L1 nodes in the queue.
* for _ in range(len(q)) allows us to dequeue L1 nodes one by one and add L2 children one by one.
* Time complexity: O(N). Space Complexity: O(N)
"""
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q, res = deque(), []
        if root != None:
            q.append(root)
        while len(q) > 0:
            level = []
            for _ in range(len(q)):
                q_node = q.popleft()
                level.append(q_node.val)
                if q_node.left != None:
                    q.append(q_node.left)
                if q_node.right != None:
                    q.append(q_node.right)
            res.append(level) 
        return res