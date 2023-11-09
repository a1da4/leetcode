# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = []
        nodes = [root]
        while nodes:
            numNodes = len(nodes)
            for _ in range(numNodes):
                node = nodes.pop(0)
                vals.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

        diff = float("inf")
        for i in range(len(vals)):
            for j in range(i+1, len(vals)):
                diff = min(diff, abs(vals[i] - vals[j]))
        return diff
