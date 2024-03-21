# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        node = head
        nextNode = getattr(node, 'next', None)
        while nextNode:
            nextNode.next, nextNode, node = node, nextNode.next, nextNode
        head.next = None
        return node
