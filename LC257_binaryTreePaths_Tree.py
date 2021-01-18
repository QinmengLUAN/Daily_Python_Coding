"""
257. Binary Tree Paths
Easy

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
# Method 1: DFS + Recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths1(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        self.dfs(root, '', res)
        return res
        
    def dfs(self, node, curr, res):
        if not node.right and not node.left:
            res.append(curr+str(node.val))
            return
        if node.right:
            self.dfs(node.right, curr+str(node.val)+"->", res)
        if node.left:
            self.dfs(node.left, curr+str(node.val)+"->", res)

# Mehod 2: BFS
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        res, dq = [], deque()
        dq.append((root, ''))
        while dq:
            for _ in range(len(dq)):
                node, curr = dq.popleft()
                if not node.left and not node.right:
                    res.append(curr + str(node.val))
                if node.left:
                    dq.append((node.left, curr + str(node.val) + "->"))
                if node.right:
                    dq.append((node.right, curr + str(node.val) + "->"))
        return res