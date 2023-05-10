# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def search(tree: Optional[TreeNode], low=-math.inf, high=math.inf) -> bool:
            if tree is None:
                return True

            if tree.val <= low or tree.val >= high:
                return False
            
            return (search(tree.left, low, tree.val) 
                    and search(tree.right, tree.val, high))
        
        return search(root)
