# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        storage = []
        answer = _head = ListNode()
        while head:
            storage.append(head.val)
            if len(storage) == k:
                while storage:
                    _head.next = ListNode(val=storage.pop())
                    _head = _head.next
            head = head.next
        
        while storage:
            _head.next = ListNode(val=storage.pop(0))
            _head = _head.next

        return answer.next

