# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        _head = head
        while _head:
            while stack and stack[-1] < _head.val:
                stack.pop()
            stack.append(_head.val)
            _head = _head.next

        answer = curr = ListNode()

        for val in stack:
            curr.next = ListNode(val)
            curr = curr.next

        return answer.next
