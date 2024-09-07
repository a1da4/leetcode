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
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        # define verify function
        def verify(lNode: Optional[ListNode], tNode: Optional[TreeNode]) -> bool:
            if lNode is None:
                return True
            if tNode is None:
                return False
            if lNode.val == tNode.val:
                return verify(lNode.next, tNode.left) or verify(lNode.next, tNode.right)
            else:
                return False
                

        # use bfs
        queue = deque([root])
        while queue:
            N = len(queue)
            for _ in range(N):
                node = queue.popleft()
                if node.val == head.val and verify(head, node):
                    return True
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return False
