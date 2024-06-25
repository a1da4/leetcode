# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.currsum = 0
        def travel(root):    
            if root is None:
                return
            travel(root.right)
            self.currsum += root.val
            root.val = self.currsum
            travel(root.left)
        
        travel(root)
        return root
