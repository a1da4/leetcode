# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def recursiveSum(node, currentSum: int, listSum: List[int]):
            if not node:
                return listSum
            
            currentSum += node.val

            if not node.left and not node.right:
                listSum.append(currentSum)
                return listSum
            
            if node.left:
                listSum = recursiveSum(node.left, currentSum, listSum)
            
            if node.right:
                listSum = recursiveSum(node.right, currentSum, listSum)
            
            return listSum
        
        listSum = recursiveSum(root, 0, [])
        return targetSum in listSum
