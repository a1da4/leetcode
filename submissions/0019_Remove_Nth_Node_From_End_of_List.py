# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        numNodes = 0
        _head = head
        while _head:
            numNodes += 1
            _head = _head.next
        
        if numNodes == 1:
            return None
        
        if numNodes == n:
            return head.next
        
        answer = _head = head
        currNode = 1
        while _head:
            if numNodes - currNode == n:
                _head.next = _head.next.next if _head.next else None
                _head = _head.next.next if _head.next else None
            else:
                _head = _head.next
            currNode += 1
        return answer
