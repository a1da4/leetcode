# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        currentNodes = deque()
        currentNodes.append(root)

        while currentNodes:
            numNodes = len(currentNodes)
            for i in range(numNodes):
                currentNode = currentNodes.popleft()
                if currentNode.val == val:
                    return currentNode

                if currentNode.left:
                    currentNodes.append(currentNode.left)
                if currentNode.right:
                    currentNodes.append(currentNode.right)
            
        return None
