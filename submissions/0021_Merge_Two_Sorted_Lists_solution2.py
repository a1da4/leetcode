# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def getVals(listn: Optional[ListNode]) -> List[int]:
            vals = []
            while listn:
                vals.append(listn.val)
                listn = listn.next
            return vals

        list12 = sorted(getVals(list1) + getVals(list2))
        answer = None
        head = None
        while list12:
            if answer == None:
                answer = ListNode(val=list12.pop(0))
                head = answer
            else:
                answer.next = ListNode(val=list12.pop(0))
                answer = answer.next

        return head
