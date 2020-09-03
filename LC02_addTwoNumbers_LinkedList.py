"""
2. Add Two Numbers
Medium: Linked List

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        node = dummy
        tmp = 0
        while l1 or l2:
            l1val, l2val = 0, 0
            if l1:
                l1val = l1.val
                l1 = l1.next
            if l2:
                l2val = l2.val
                l2 = l2.next
            value = (tmp + l1val + l2val) % 10
            tmp = (tmp + l1val + l2val) // 10
            node.next = ListNode(value)
            node = node.next

        if tmp != 0:
            node.next = ListNode(tmp)
        return dummy.next