# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessHead = lessNodes = ListNode()
        largeHead = largeNodes = ListNode()

        while head:
            if head.val < x:
                lessNodes.next = ListNode(val=head.val)
                lessNodes = lessNodes.next
            else:
                largeNodes.next = ListNode(val=head.val)
                largeNodes = largeNodes.next
            head = head.next
        
        lessNodes.next = largeHead.next

        return lessHead.next
