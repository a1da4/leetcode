"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        checked = set()

        for node in tree:
            if not node:
                continue
            for child in node.children:
                checked.add(child)
        
        for node in tree:
            if node not in checked:
                return node

