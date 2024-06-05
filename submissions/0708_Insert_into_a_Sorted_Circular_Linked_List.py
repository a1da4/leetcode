"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            head = Node(val=insertVal)
            head.next = head
        else:
            prev, curr = head, head.next
            is_here = False

            while True:
                if prev.val <= insertVal <= curr.val:
                    is_here = True
                elif prev.val > curr.val:
                    if insertVal >= prev.val or insertVal <= curr.val:
                        is_here = True
                else:
                    pass

                if is_here:
                    prev.next = Node(insertVal, curr)
                    return head

                prev, curr = curr, curr.next
                if prev == head:
                    break
            prev.next = Node(insertVal, curr)

        return head

