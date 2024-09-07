# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
                 1
4                                4                      
    2                         2
  1                       6         8           
                                  1    3

BFS
Q = [1]


def check(treenode, head):
    if not head:
        return True
    
    if not treenode:
        return False
    
    for left, right in treenode.left, treenode.right:
        if left.val == head.next.val:
            check
        


head = [1, 4, 2, 6]

"""

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def check(treenode, head):
            if not head:
                return True
            
            if not treenode:
                return False
            
            if treenode.val != head.val:
                return False
            
            left = check(treenode.left, head.next)
            right = check(treenode.right, head.next)
                
            return left or right
        
        Q = deque([root])
        
        while Q:
            node = Q.popleft()
            if node.val == head.val and check(node, head):
                return True
            for child in node.left, node.right:
                if child:
                    Q.append(child)
            
        return False
        