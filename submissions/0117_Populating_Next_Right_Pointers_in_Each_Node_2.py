"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        answer = root
        if root:
            nodes = [root]
            while nodes:
                numNodes = len(nodes)
                prevNode = None
                for _ in range(numNodes):
                    node = nodes.pop(0)
                    if prevNode:
                        prevNode.next = node
                    prevNode = node
                    if node.left:
                        nodes.append(node.left)
                    if node.right:
                        nodes.append(node.right)

        return answer
