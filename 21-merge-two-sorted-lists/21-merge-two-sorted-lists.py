# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()

        while l1 or l2:
            val_1 = l1.val if l1 else float("inf")
            val_2 = l2.val if l2 else float("inf")

            cur.next = ListNode(min(val_1, val_2))
            cur = cur.next

            if val_1 < val_2:
                l1 = l1.next
            else:
                l2 = l2.next

        return dummy.next