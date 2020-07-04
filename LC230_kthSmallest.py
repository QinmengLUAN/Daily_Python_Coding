"""
230. Kth Smallest Element in a BST
Medium: Binary search, tree

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Constraints:

The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
Accepted
397,408
Submissions
666,433
Seen this question in a real interview before?

Yes

No
Contributor
shtian
Try to utilize the property of a BST.
Try in-order traversal. (Credits to @chan13)
What if you could modify the BST node's structure?
The optimal runtime complexity is O(height of BST).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursion O(N)
    """
    It's a very straightforward approach with \mathcal{O}(N)O(N) time complexity. The idea is to build an inorder traversal of BST which is an array sorted in the ascending order. Now the answer is the k - 1th element of this array.
    Complexity Analysis
    Time complexity : \mathcal{O}(N)O(N) to build a traversal.
    Space complexity : \mathcal{O}(N)O(N) to keep an inorder traversal.
    """
    def kthSmallest1(self, root: TreeNode, k: int) -> int:
        nums = self.helper(root, [])
        return nums[k - 1]
    def helper(self, root, nums):
        if root == None:
            return []
        self.helper(root.left, nums)
        nums.append(root.val)
        self.helper(root.right, nums)
        return nums
    # Iteration
    """
    Time complexity : \mathcal{O}(H + k)O(H+k), where HH is a tree height. This complexity is defined by the stack, which contains at least H + kH+k elements, since before starting to pop out one has to go down to a leaf. This results in \mathcal{O}(\log N + k)O(logN+k) for the balanced tree and \mathcal{O}(N + k)O(N+k) for completely unbalanced tree with all the nodes in the left subtree.
    Space complexity : \mathcal{O}(H + k)O(H+k), the same as for time complexity, \mathcal{O}(N + k)O(N+k) in the worst case, and \mathcal{O}(\log N + k)O(logN+k) in the average case.
    """
    def kthSmallest(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right