# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        1. Can have repeated nums.
        2. Can be empty
        3. Can be of unequal length
        
        Algorithm:
        1. If either list is empty, return the other list. [NOT NEEDED]
        2. Save the smallest head. [NOT NEEDED]
        3. Create a dummy head.
        4. Use two pointers technique to merge the two lists
        
        
        '''
        
        dummy = cur = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        
        cur.next = list1 or list2
        
        return dummy.next
                