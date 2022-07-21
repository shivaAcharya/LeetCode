# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # if left == right:
        #     return head
        
        # Find before_left and left_node
        before_left, left_node = None, head
        
        for _ in range(left - 1):
            before_left = left_node
            left_node = left_node.next
        
        # Reverse nodes between left and right
        prev, cur = None, left_node
        #print(before_left.val, left_node.val)
        for _ in range(right - left + 1):
            nxt = cur.next 
            cur.next = prev
            prev = cur
            cur = nxt
        
        # Link before_left and left_node
        left_node.next = cur
        if not before_left:
            return prev
        
        
        before_left.next = prev       
        
        return head
        