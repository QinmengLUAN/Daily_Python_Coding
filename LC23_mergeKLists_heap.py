"""
23. Merge k Sorted Lists
Hard: Linked list, heapq
My first Hard question.

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # from heapq import heappush, heappop
        dummy = temp = ListNode()
        
        hq = [(lists[i].val, i, lists[i]) for i in range(len(lists)) if lists[i]]
        heapify(hq)
        
        ## The above two lines can be replaced to:         
        # if not len(lists):
        #     return None
        # hq = []
        # for i in range(len(lists)):
        #     if lists[i]:
        #         heapq.heappush(hq, (lists[i].val, i, lists[i]))
        
        while hq:
            val, idx, temp.next = heapq.heappop(hq)
            temp = temp.next
            if temp.next:
                heapq.heappush(hq, (temp.next.val, idx, temp.next))
        
        return dummy.next
