# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ansHead = ListNode()
        ansHead.next = head
        currSum = 0
        sum2node = {currSum: ansHead}
        while head:
            currSum += head.val
            sum2node[currSum] = head
            head = head.next
        head = ansHead
        currSum = 0
        while head:
            currSum += head.val
            head.next = sum2node[currSum].next
            head = head.next
        return ansHead.next
