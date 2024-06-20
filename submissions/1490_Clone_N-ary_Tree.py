"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        copyNode = Node(root.val)
        for child in root.children:
            copyNode.children.append(self.cloneTree(child))
        
        return copyNode

