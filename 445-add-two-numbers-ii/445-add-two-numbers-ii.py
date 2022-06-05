# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list(head):
            prev, cur = None, head

            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            return prev
        
        new_l1, new_l2 = reverse_list(l1), reverse_list(l2)
        dummy = cur = ListNode()
        carry = 0

        while new_l1 or new_l2 or carry:
            l1_val = new_l1.val if new_l1 else 0
            l2_val = new_l2.val if new_l2 else 0

            cur_sum, carry = (l1_val + l2_val + carry) % 10, (l1_val + l2_val + carry) // 10

            cur.next = ListNode(cur_sum)
            cur = cur.next

            new_l1 = new_l1.next if new_l1 else None
            new_l2 = new_l2.next if new_l2 else None
        
        return reverse_list(dummy.next)