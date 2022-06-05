# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None

        # Calculate length of linked list
        N, cur = 1, head
        while cur.next:
            N += 1
            cur = cur.next

        tail_node = cur

        # Update k
        k = k % N


        # Return head if k == N
        if k == N or k == 0:
            return head

        # Second pass till N-k
        prev, cur = None, head

        for _ in range(N-k):
            prev, cur = cur, cur.next

        # Update pointers
        tail_node.next = head
        prev.next = None

        return cur

    """
    Time => O(N + (N-N % k)) ~ O(N)
    Space => O(1)
    """