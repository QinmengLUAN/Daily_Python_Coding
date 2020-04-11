"""
160. Intersection of Two Linked Lists
Easy: Linked list, lengths of lists before the intersection point is important
Algorithm: calculate length of headA and headB, get the length of each list, pop items to get lists with the same length

Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
begin to intersect at node c1.
Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 
Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = 0
        lenB = 0
        curr_nodeA = headA
        curr_nodeB = headB    
        while curr_nodeA != None:
            lenA += 1
            curr_nodeA = curr_nodeA.next
        while curr_nodeB != None:
            lenB += 1
            curr_nodeB = curr_nodeB.next
        if lenA > lenB:
            for i in range(abs(lenA - lenB)):
                headA = headA.next
        if lenA < lenB:
             for i in range(abs(lenA - lenB)):
                headB = headB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA