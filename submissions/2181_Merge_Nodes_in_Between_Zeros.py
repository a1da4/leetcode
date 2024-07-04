# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        _head = head
        while _head:
            __head = _head.next
            while __head.val != 0:
                _head.val += __head.val
                __head = __head.next
            _head.next = __head.next
            _head = _head.next

        return head

