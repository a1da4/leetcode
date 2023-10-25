# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        numNodes = 0
        id2val = {}
        while head:
            id2val[numNodes] = head.val
            numNodes += 1
            head = head.next
        if numNodes == 0:
            return None
        rest = k % numNodes
        startId = numNodes - rest if rest > 0 else 0
        answer = _head = ListNode()
        for i in range(numNodes):
            currId = (startId + i) % numNodes
            _head.next = ListNode(val=id2val[currId])
            _head = _head.next

        return answer.next
