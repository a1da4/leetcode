# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.maxLen = 0

        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return [0, 0]
            
            numInc = 1
            numDec = 1
            if node.left:
                left = dfs(node.left)
                if node.val == node.left.val + 1:
                    numInc = left[0] + 1
                elif node.val + 1 == node.left.val:
                    numDec = left[1] + 1
            
            if node.right:
                right = dfs(node.right)
                if node.val == node.right.val + 1:
                    numInc = max(numInc, right[0] + 1)
                elif node.val + 1 == node.right.val:
                    numDec = max(numDec, right[1] + 1)

            self.maxLen = max(self.maxLen, numInc + numDec - 1)

            return [numInc, numDec]
        
        dfs(root)
        return self.maxLen

