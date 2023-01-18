# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        1. Reverse the second half of the linked list.
        2. Check for palindromicity.        
        '''
        
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse the second half
        prev, cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # Check for palindromicity
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        
        return True
        
        '''
        1 -> 2 -> 3 -> 2 -> 1
        
        None <- 3 <- 2 <- 1
        
        '''
        