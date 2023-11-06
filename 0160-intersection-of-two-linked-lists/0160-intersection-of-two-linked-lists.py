# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        curA, curB = headA, headB
        curA_switched = curB_switched = False
        
        while curA and curB and curA != curB:
            curA = curA.next
            curB = curB.next
            
            if not curA and not curA_switched:
                curA = headB
                curA_switched = True
            
            if not curB and not curB_switched:
                curB = headA
                curB_switched = True
        
        if not curA or not curB:
            return
        
        return curA
