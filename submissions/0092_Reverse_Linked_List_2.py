# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        targetId2val = {}
        currId = 1
        _head = head
        while _head:
            if left <= currId <= right:
                targetId2val[right-currId+left] = _head.val
            _head = _head.next
            currId += 1
        
        answer = _head = head
        currId = 1
        while _head:
            if left <= currId <= right:
                _head.val = targetId2val[currId]
            _head = _head.next
            currId += 1

        return answer
