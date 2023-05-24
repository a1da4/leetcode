# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeVocab = set()
        while head:
            if head in nodeVocab:
                return True
            else:
                nodeVocab.add(head)
            head = head.next
        return False
