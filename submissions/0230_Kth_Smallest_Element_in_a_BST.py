# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root: Optional[TreeNode]) -> List[int]:
            vals = []
            if root:
                vals = inorder(root.left)
                vals.append(root.val)
                vals = vals + inorder(root.right)
            return vals
        
        vals = inorder(root)
        
        return vals[k-1]
