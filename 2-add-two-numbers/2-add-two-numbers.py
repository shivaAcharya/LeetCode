# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node
        dummy = cur = ListNode()
        
        carry = 0
        
        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            
            sum_val, carry = (num1 + num2 + carry) % 10 , (num1 + num2 + carry) // 10
            
            # Create new node and link cur to it
            cur.next = ListNode(sum_val)
            
            # Update cur
            cur = cur.next
            
            # Update l1 and l2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next

"""
DRY RUN

l1 = 9
l2 = 0

sum_val = 8
carry = 1

dummy -> 8


"""