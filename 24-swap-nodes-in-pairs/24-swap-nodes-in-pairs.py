# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()            # 
        prevP = dummy                 #
        dummy.next = head            # always points to the head
        currentP = head                # points to 1
                        # 2                    1
        while(currentP != None and currentP.next != None):
            nextP = currentP.next        # 2
            
            currentP.next = nextP.next   # 1.next = 2.next (3)
            nextP.next = currentP        # 2.next = 1
            prevP.next = nextP           # dummy -> 2

            prevP = currentP            # 1
            currentP = currentP.next    # 3

        return dummy.next  