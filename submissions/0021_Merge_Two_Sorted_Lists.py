# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = None
        val2 = None
        answer = None
        head = None
        while list1 or list2:
            if val1 == None and list1:
                val1 = list1.val
                list1 = list1.next
            if val2 == None and list2:
                val2 = list2.val
                list2 = list2.next
            if val1 != None and val2 == None:
                if answer == None:
                    answer = ListNode(val=val1)
                    head = answer
                else:
                    answer.next = ListNode(val=val1)    
                    answer = answer.next
                val1 = None
            elif val1 == None and val2 != None:
                if answer == None:
                    answer = ListNode(val=val2)
                    head = answer
                else:
                    answer.next = ListNode(val=val2)
                    answer = answer.next
                val2 = None
            elif val1 <= val2:
                if answer == None:
                    answer = ListNode(val=val1)
                    head = answer
                else:
                    answer.next = ListNode(val=val1)    
                    answer = answer.next
                val1 = None
            else:
                if answer == None:
                    answer = ListNode(val=val2)
                    head = answer
                else:
                    answer.next = ListNode(val=val2)
                    answer = answer.next
                val2 = None

        if val1 != None:
            answer.next = ListNode(val=val1)
        if val2 != None:
            answer.next = ListNode(val=val2)

        return head
