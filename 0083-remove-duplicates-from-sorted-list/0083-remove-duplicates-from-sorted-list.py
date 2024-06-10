# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        
        dummy = cur = ListNode(head)
        
    
        while head:
            if head.val != cur.val:
                cur.next = ListNode(head.val)
                cur = cur.next
            head = head.next
    
        return dummy.next