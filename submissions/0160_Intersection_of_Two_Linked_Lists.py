# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeVocab = set()
        while headA:
            nodeVocab.add(headA)
            headA = headA.next
        
        skipB = 0
        while headB:
            if headB in nodeVocab:
                return headB
            skipB += 1
            headB = headB.next
        return
