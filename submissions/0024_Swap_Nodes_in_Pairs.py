# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = None
        answerRoot = answer = ListNode()

        while head:
            if tmp is None:
                tmp = head.val
            else:
                answer.next = ListNode(head.val)
                answer = answer.next
                answer.next = ListNode(tmp)
                answer = answer.next
                tmp = None            
            head = head.next
        if tmp is not None:
            answer.next = ListNode(tmp)

        return answerRoot.next
