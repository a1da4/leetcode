# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        for root in lists:
            while root:
                vals.append(root.val)
                root = root.next
        
        root = answer = ListNode()
        for val in sorted(vals):
            root.next = ListNode(val=val)
            root = root.next
        return answer.next
