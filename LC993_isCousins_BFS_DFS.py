"""
993. Cousins in Binary Tree
Easy

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:
Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS solution
    def isCousins1(self, root: TreeNode, x: int, y: int) -> bool:
        nodes = {} # key: node.val, value: [level, parent.val]
        dq = deque()
        dq.append((root, 0, 0)) # curr_layer stores (node, level, parent.val)

        while len(dq) > 0:
            node, level, parent = dq.popleft()
            nodes[node.val] = [level, parent]
            if node.left:
                dq.append((node.left, level+1, node.val))
            if node.right:
                dq.append((node.right, level+1, node.val))
        if nodes[x][0] == nodes[y][0] and nodes[x][1] != nodes[y][1]:
            return True
        return False
    
    # DFS solution
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        lx,px = self.dfs(root, 0, 0, x) # input: node. level, parent, x
        ly,py = self.dfs(root, 0, 0, y) 
        if lx == ly and px != py:
            return True
        return False
    def dfs(self, node, level, parent, mod):
        if node == None:
            return None
        if node.val == mod:
            return level, parent
        return self.dfs(node.left, level+1, node.val, mod) or self.dfs(node.right, level+1, node.val, mod)