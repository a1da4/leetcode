# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        currNodes = [root]
        numNodes = 0
        while currNodes:
            numCurrNodes = len(currNodes)
            for _ in range(numCurrNodes):
                currNode = currNodes.pop(0)
                numNodes += 1
                if currNode.left:
                    currNodes.append(currNode.left)
                if currNode.right:
                    currNodes.append(currNode.right)
        
        return numNodes
