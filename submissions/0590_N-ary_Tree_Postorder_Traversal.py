"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        self.answer = []
        def travel(node):
            if not node:
                return
            for child in node.children:
                travel(child)
            
            self.answer.append(node.val)
        
        travel(root)

        return self.answer

