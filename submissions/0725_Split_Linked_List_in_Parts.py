# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        answer = [None for _ in range(k)]

        _head = head
        num = 0
        while _head:
            num += 1
            _head = _head.next
        
        each, rest = num // k, num % k

        _head = head
        for i in range(k):
            dt = 1 if i < rest else 0
            if each + dt == 0:
                break
            
            root = ListNode()
            curr = root
            for _ in range(each + dt):
                curr.next = ListNode(_head.val)
                curr = curr.next
                _head = _head.next
            
            answer[i] = root.next


        return answer

