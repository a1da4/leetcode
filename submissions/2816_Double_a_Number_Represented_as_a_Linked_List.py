# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        while head:
            total = total * 10 + head.val
            head = head.next

        total *= 2
        answer = curr = ListNode()
        if total == 0:
            return answer
        
        vals = []
        while total:
            vals.append(total % 10)
            total = total // 10
        
        for val in vals[::-1]:
            curr.next = ListNode(val)
            curr = curr.next

        return answer.next

