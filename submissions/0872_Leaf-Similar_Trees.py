# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def getLeaves(root: Optional[TreeNode], leaves: List[int]) -> List[int]:
            if root.left is None and root.right is None:
                leaves.append(root.val)
                return leaves
            if root.left:
                getLeaves(root.left, leaves)
            if root.right:
                getLeaves(root.right, leaves)
            
            return leaves
        
        leaves1 = getLeaves(root1, [])
        leaves2 = getLeaves(root2, [])

        if len(leaves1) != len(leaves2):
            return False
        for leave1, leave2 in zip(leaves1, leaves2):
            if leave1 != leave2:
                return False
        return True 
