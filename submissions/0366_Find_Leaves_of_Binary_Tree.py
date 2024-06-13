# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        _vals = []
        
        def nextIsLeaf(node: Optional[TreeNode]) -> bool:
            return not node.left and not node.right

        def searchLeaves(node: Optional[TreeNode]):
            if not node.left:
                pass
            elif nextIsLeaf(node.left):
                vals.append(node.left.val)
                node.left = None
            else:
                searchLeaves(node.left)
            if not node.right:
                pass
            elif nextIsLeaf(node.right):
                vals.append(node.right.val)
                node.right = None
            else:
                searchLeaves(node.right)

        while root:
            vals = []
            searchLeaves(root)
            if vals:
                _vals.append(vals)
            if not root.left and not root.right:
                _vals.append([root.val])
                root = None

        return _vals
        
