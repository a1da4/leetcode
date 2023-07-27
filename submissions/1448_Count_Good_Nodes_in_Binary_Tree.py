# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        thresh = root.val

        def countGood(node, thresh: int, count: int) -> int:
            if not node:
                return count
            
            if node.val >= thresh:
                count += 1
                thresh = node.val
            if node.left:
                count = countGood(node.left, thresh, count)
            if node.right:
                count = countGood(node.right, thresh, count)

            return count
        
        count = countGood(root, thresh, 0)

        return count
