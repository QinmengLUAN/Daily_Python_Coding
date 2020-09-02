"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
Here is the function signature as a starting point (in Python):

"""
# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.
    dummy = ListNode(0)
    node = dummy
    tmp = 0
    while l1 or l2:
        node.next = ListNode(0)
        node = node.next
        if l1 and l2:
            value = (tmp + l1.val + l2.val) % 10
            tmp = (tmp + l1.val + l2.val) // 10
            node.val = value
            l1 = l1.next
            l2 = l2.next
        elif l1:
            value = (tmp + l1.val) % 10
            tmp = (tmp + l1.val) // 10
            node.val = value
            l1 = l1.next           
        elif l2:
            value = (tmp + l2.val) % 10
            tmp = (tmp + l2.val) // 10
            node.val = value
            l2 = l2.next 
    
    if tmp != 0:
        node.next = ListNode(0)
        node = node.next
        node.val = tmp
    return dummy.next
########################################
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 7 0 8