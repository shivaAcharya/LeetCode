# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr1, ptr2 = headA, headB
        reach_end = False

        while ptr1 != ptr2:
            ptr1, ptr2 = ptr1.next, ptr2.next

            if not ptr1:
                if not reach_end:
                    reach_end = True
                    ptr1 = headB
                else:
                    return None

            if not ptr2:
                ptr2 = headA

        return ptr1