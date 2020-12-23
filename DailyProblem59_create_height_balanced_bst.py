"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a sorted list, create a height balanced binary search tree, meaning the height differences of each node can only differ by at most 1.

Here's some code to start with:

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    answer = str(self.value)
    if self.left:
      answer += str(self.left)
    if self.right:
      answer += str(self.right)
    return answer

def create_height_balanced_bst(nums):
  # Fill this in.

tree = create_height_balanced_bst([1, 2, 3, 4, 5, 6, 7, 8])
# 53214768
#  (pre-order traversal)
#       5
#      / \
#     3    7
#    / \  / \
#   2   4 6  8
#  /
# 1
"""
"""
Algorithm:
In the previous post, we discussed construction of BST from sorted Linked List. Constructing from sorted array in O(n) time is simpler as we can get the middle element in O(1) time. Following is a simple algorithm where we first find the middle node of list and make it root of the tree to be constructed.
1) Get the Middle of the array and make it root.
2) Recursively do same for left half and right half.
      a) Get the middle of left half and make it left child of the root
          created in step 1.
      b) Get the middle of right half and make it right child of the
          root created in step 1
"""
class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    answer = str(self.value)
    if self.left:
      answer += str(self.left)
    if self.right:
      answer += str(self.right)
    return answer

def create_height_balanced_bst(nums):
  # Fill this in.
  if len(nums) == 0:
    return None
  # find middle
  mid = len(nums) // 2
  # make the middle element the root
  root = Node(nums[mid])
  root.left = create_height_balanced_bst(nums[:mid])
  root.right = create_height_balanced_bst(nums[mid+1:])
  return root

tree = create_height_balanced_bst([1, 2, 3, 4, 5, 6, 7, 8])
print(tree)
# 53214768