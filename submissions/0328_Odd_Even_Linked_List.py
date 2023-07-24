# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return None
        headOdd = head
        headEven = head.next
        headEven_ = headEven

        while headOdd and headEven and headOdd.next and headEven.next:
            headOdd.next = headEven.next
            headOdd = headOdd.next
            headEven.next = headOdd.next
            headEven = headEven.next
        
        headOdd.next = headEven_

        return head
