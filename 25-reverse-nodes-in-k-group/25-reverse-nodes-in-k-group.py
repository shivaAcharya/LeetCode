# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        
        new_head = None
        L = 0
        cur = head
        while cur:
            L += 1
            cur = cur.next
        
        cur = head
        
        while L >= k:
            L -= k
            cur_head, prev = cur, None
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                            
            if not new_head:
                new_head = prev
            
            if cur:
                tmp = cur
                for _ in range(k-1):
                    if tmp:
                        tmp = tmp.next
                cur_head.next = tmp if tmp else cur
        
        return new_head