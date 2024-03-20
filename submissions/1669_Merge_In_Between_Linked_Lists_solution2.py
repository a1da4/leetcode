# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        currNode = list1
        currId = 0

        while currNode:
            if currId + 1 == a:
                node12 = currNode
            if currId - 1 == b:
                node21 = currNode
            currNode = currNode.next
            currId += 1

        currNode = list2
        while currNode:
            if currNode.next is None:
                node2 = currNode
            currNode = currNode.next
        
        node12.next = list2
        node2.next = node21

        return list1

