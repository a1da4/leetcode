# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        while root:
            if root.next is None:
                break
            
            tmp = root.next
            root.next = ListNode(math.gcd(root.val, tmp.val))
            root.next.next = tmp

            root = root.next.next

        return head
