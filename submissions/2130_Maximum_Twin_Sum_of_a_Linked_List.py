# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = deque()
        while head:
            nums.append(head.val)
            head = head.next
        
        maxSum = 0
        while nums:
            currSum = nums.popleft() + nums.pop()
            maxSum = max(currSum, maxSum)
        
        return maxSum
