"""
206. Reverse Linked List
Easy: Linked list, iterative

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. 
Could you implement both?
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode: 
        if head == None or head.next == None:
            return head
        
        curr = head 
        curr_next = head.next
        curr.next = None

        while curr_next != None:
            tem = curr_next.next
            curr_next.next = curr
            curr = curr_next
            curr_next = tem
        return curr