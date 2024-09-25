# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle of list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next       
        
        # Reverse second half
        cur = slow.next
        prev = slow.next = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # Merge two linked lists
        temp = cur = ListNode()
        while prev:
            cur.next = head
            head = head.next
            cur = cur.next
            cur.next = prev
            prev = prev.next
            cur = cur.next
            
        cur.next = head
        