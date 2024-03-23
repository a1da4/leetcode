# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        vals = []
        _head = head
        while _head:
            vals.append(_head.val)
            _head = _head.next

        _head = head
        _head.val = vals.pop(0)
        rev = True
        while vals:
            if rev:
                _head.next = ListNode(val=vals.pop())
                rev = False
            else:
                _head.next = ListNode(val=vals.pop(0))
                rev = True
            _head = _head.next

