# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        for tree in lists:
            while tree:
                heapq.heappush(vals, tree.val)
                tree = tree.next

        root = answer = ListNode()        
        while vals:
            val = heapq.heappop(vals)
            answer.next = ListNode(val = val)
            answer = answer.next
        
        return root.next
