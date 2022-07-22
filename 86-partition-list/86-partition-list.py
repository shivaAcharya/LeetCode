# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        less_than = [1, 2, 2]
        greater_than = [4, 5]
        
        """
        less_than_x = less = ListNode()
        x_or_greater = more = ListNode()
    
        
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                more.next = head
                more = more.next
            head = head.next
        
        more.next = None
        less.next = x_or_greater.next
        
        return less_than_x.next