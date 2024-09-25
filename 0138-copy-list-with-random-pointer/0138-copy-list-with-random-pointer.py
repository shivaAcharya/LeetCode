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
        old_to_new = {}
        temp = new_cur = ListNode()
        cur = head
        
        while cur:
            # new_node = ListNode(cur.val)
            new_cur.next = ListNode(cur.val)
            new_cur = new_cur.next
            old_to_new[cur] = new_cur
            cur = cur.next
        
        new_cur = temp.next
        cur = head
        while cur:
            if not cur.random:
                new_cur.random = None
            else:
                new_cur.random = old_to_new[cur.random]
            new_cur = new_cur.next
            cur = cur.next
        
        return temp.next
        