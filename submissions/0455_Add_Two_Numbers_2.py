# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = ""
        while l1:
            val1 += str(l1.val)
            l1 = l1.next
        
        val2 = ""
        while l2:
            val2 += str(l2.val)
            l2 = l2.next

        num = int(val1) + int(val2)

        answer = curr = ListNode()
        for val in str(num):
            curr.next = ListNode(int(val))
            curr = curr.next
        
        return answer.next

