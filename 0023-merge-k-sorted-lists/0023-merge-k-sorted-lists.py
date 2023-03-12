# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Handle corner cases
        if not lists: return

        def merge_two_sorted_lists(l1, l2):
            dummy = cur = ListNode()

            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next

            cur.next = l1 or l2
            return dummy.next

        while len(lists) > 1:

            mergedLists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i + 1 < len(lists) else None # Handle list with odd lists
                mergedLists.append(merge_two_sorted_lists(list1, list2))

            lists = mergedLists

        return lists[0]

"""
Time Complexity => O(Nlogk) -> N is total number of nodes, k is number of linked lists
Space Complexity => O(1)

"""