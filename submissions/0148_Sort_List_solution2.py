# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        while head:
            heapq.heappush(vals, head.val)
            head = head.next

        answer = root = ListNode()
        while vals:
            val = heapq.heappop(vals)
            root.next = ListNode(val=val)
            root = root.next
        
        return answer.next
