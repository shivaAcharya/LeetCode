# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = cur = ListNode()
        carry = 0
        
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            cur_sum = num1 + num2 + carry
            cur_num, carry = cur_sum % 10, cur_sum // 10
            cur.next = ListNode(cur_num)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            cur.next = ListNode(carry)
        
        return dummy.next
            