# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forest = []
        delItems = set(to_delete)

        def _search(node, delItems, forest):
            if not node:
                return None
            node.left = _search(node.left, delItems, forest)
            node.right = _search(node.right, delItems, forest)

            if node.val in delItems:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None
            
            return node
        
        root = _search(root, delItems, forest)
        if root:
            forest.append(root)
        
        return forest
