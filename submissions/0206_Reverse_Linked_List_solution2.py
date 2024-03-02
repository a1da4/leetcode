# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        answer = root = ListNode()
        for val in vals[::-1]:
            root.next = ListNode(val=val)
            root = root.next
        
        return answer.next
