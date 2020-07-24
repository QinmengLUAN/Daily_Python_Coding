"""
83. Remove Duplicates from Sorted List
Easy: Linked list

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sb = head
        while sb != None:
            while sb.next != None and sb.val == sb.next.val:
                sb.next = sb.next.next
            sb = sb.next
        return head