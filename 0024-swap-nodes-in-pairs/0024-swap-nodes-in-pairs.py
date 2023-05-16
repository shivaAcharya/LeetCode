# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode()
        dummy.next = head
        cur = head

        while cur and cur.next:
            # Save next ptr
            nxt = cur.next
            cur.next = nxt.next

            # Swap nodes
            prev.next = nxt
            nxt.next = cur

            # Update ptrs
            prev = cur
            cur = cur.next

        return dummy.next