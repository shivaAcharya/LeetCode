# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode()
        # nums_set for O(1) lookup
        
        # W
        
        dummy = cur = ListNode()
        nums_set = set(nums)
        
        while head:
            # print(cur.val)
            if head.val not in nums_set:
                cur.next = ListNode(head.val)
                cur = cur.next
            head = head.next
        
        return dummy.next
    