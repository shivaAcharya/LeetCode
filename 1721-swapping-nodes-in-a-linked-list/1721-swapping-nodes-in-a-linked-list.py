# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        slow = fast = head
        
        # Move fast kth steps
        for _ in range(k - 1):
            fast = fast.next
        
        node_1 = fast
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.val, node_1.val = node_1.val, slow.val
    
        return head