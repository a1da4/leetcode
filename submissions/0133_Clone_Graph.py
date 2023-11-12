"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldNode2newNode = {}
        def dfs(node):
            if not node:
                return None
            if node in oldNode2newNode:
                return oldNode2newNode[node]
            newNode = Node(val=node.val)
            oldNode2newNode[node] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            return newNode

        return dfs(node)
