# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        prev = None
        
        while head:
            if head.next and head.val == head.next.val:
                prev = head.val
                # head = head.next.next
            elif head.val != prev:
                cur.next = head
                cur = cur.next
            head = head.next
        cur.next = None
        return dummy.next