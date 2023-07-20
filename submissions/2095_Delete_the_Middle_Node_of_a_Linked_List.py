# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        depth = 0
        temp = head
        while temp:
            depth += 1
            temp = temp.next

        target = depth // 2 + 1
        answer = head

        if depth == 1:
            answer = None
        elif depth == 2:
            head.next = None
        else:
            prevNode = None
            while head:
                target -= 1
                if target == 1:
                    prevNode = head
                if target == -1:
                    prevNode.next = head
                head = head.next

        return answer
