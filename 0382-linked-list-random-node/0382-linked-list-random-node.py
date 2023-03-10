# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = 0
        # Calculate length
        cur = self.head
        while cur:
            self.length += 1
            cur = cur.next

    def getRandom(self) -> int:
        random_num = random.randrange(1, self.length + 1)
        cur = self.head
        for _ in range(random_num - 1):
            cur = cur.next
        return cur.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()