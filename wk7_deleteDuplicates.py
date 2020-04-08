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
        sb2 = head
        while sb2 != None and sb2 != None:
            while sb2.next != None and sb2.val == sb2.next.val:
                sb2 = sb2.next
            sb2 = sb2.next
            sb.next = sb2
            sb = sb2
        return head