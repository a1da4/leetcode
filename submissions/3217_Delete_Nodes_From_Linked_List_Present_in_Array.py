# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        answer = ListNode()
        curr = answer
        while head:
            if head.val not in nums:
                curr.next = ListNode(val=head.val)
                curr = curr.next

            head = head.next
            
        return answer.next
