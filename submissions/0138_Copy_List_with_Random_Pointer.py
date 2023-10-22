"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        answerHead = answer = Node(0)

        _head = head
        old2new = {}

        while _head:
            answer.next = Node(x=_head.val)
            answer = answer.next
            old2new[_head] = answer
            _head = _head.next

        _head = head
        answer = answerHead.next
        while _head:
            if _head.random:
                answer.random = old2new[_head.random]
            answer = answer.next
            _head = _head.next
        
        return answerHead.next
