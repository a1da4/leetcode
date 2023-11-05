# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def sumNumbersIter(root: Optional[TreeNode], currSum: int):
            currSum = currSum * 10 + root.val
            if root.left is None and root.right is None:
                return currSum

            leftSum = rightSum = 0
            if root.left:
                leftSum = sumNumbersIter(root.left, currSum)
            if root.right:
                rightSum = sumNumbersIter(root.right, currSum)
            return leftSum + rightSum
        
        return sumNumbersIter(root, 0)
