# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        vals = []
        def bst(node):
            if node is None:
                return
            bst(node.left)
            vals.append(node.val)
            bst(node.right)

        bst(root)
        
        if len(vals) == 1:
            return True

        for val_0, val_1 in zip(vals[:-1], vals[1:]):
            if val_0 >= val_1:
                return False
        
        return True
