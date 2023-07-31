# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        maxSum = None
        maxDepth = 0
        currDepth = 0
        currNodes = deque()
        currNodes.append(root)

        while currNodes:
            currDepth += 1
            numNodes = len(currNodes)
            currSum = 0
            for i in range(numNodes):
                currNode = currNodes.popleft()
                currSum += currNode.val

                if currNode.left:
                    currNodes.append(currNode.left)
                if currNode.right:
                    currNodes.append(currNode.right)
        
            if maxSum is None or currSum > maxSum:
                maxSum = currSum
                maxDepth = currDepth
        
        return maxDepth
