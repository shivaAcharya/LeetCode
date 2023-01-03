# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1. Can be empty linked list.
        2. If only one node, return the node
        
        
        Algorithm
        1. Use prev, cur, and nxt pointers.
        2. While cur and cur.next:
        3.  nxt = cur.next => cur.next = prev => prev = cur => cur = nxt
        4. Return prev
                
        '''
        cur, prev = head, None
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return prev