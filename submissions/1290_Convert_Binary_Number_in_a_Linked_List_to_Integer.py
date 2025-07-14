# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        digits_str = ""
        while head:
            digits_str += str(head.val)
            head = head.next
        
        return int(digits_str, 2)
