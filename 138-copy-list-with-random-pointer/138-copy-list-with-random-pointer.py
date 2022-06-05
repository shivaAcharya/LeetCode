"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_new = {}
        dummy = cur_new = ListNode(0)
        cur_old = head

        # Create mapping
        while cur_old:
            cur_new.next = ListNode(cur_old.val)
            cur_new = cur_new.next
            old_new[cur_old] = cur_new
            cur_old = cur_old.next
        
        # Link random pointers
        cur_old, cur_new = head, dummy.next
        while cur_old:
            cur_new.random = old_new.get(cur_old.random, None)
            cur_old, cur_new = cur_old.next, cur_new.next
        
        return dummy.next
    """
    Time Complexity => O(n)
    Space Complexity => O(n)
    """