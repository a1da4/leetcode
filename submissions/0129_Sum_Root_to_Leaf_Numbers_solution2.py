# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def calculateSum(node: TreeNode, currentSum: int) -> int:
            if not node:
                return 0
            
            currentSum = currentSum * 10 + node.val
            
            if not node.left and not node.right:
                return currentSum

            leftSum = calculateSum(node.left, currentSum)
            rightSum = calculateSum(node.right, currentSum)
            
            return leftSum + rightSum

        return calculateSum(root, 0)

