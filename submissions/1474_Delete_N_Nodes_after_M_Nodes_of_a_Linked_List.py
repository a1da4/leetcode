# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        curr = head
        while curr:
            for _ in range(m - 1):
                curr = curr.next
                if curr is None:
                    break
            if curr is None:
                break
            _curr = curr
            for _ in range(n + 1):
                _curr = _curr.next
                if _curr is None:
                    break
            curr.next = _curr
            curr = curr.next
        return head
