# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode()
        dummy.next = cur = head

        while cur and cur.next:
            # Save next nodes
            nxt = cur.next
            cur.next = nxt.next

            # Move pointers
            prev.next = nxt
            nxt.next = cur

            # Update pointers
            prev = cur
            cur = cur.next

        return dummy.next
    