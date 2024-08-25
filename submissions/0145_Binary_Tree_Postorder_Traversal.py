# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.answer = []

        def travel(node: Optional[TreeNode]):
            if not node:
                return
            if node.left:
                travel(node.left)
            if node.right:
                travel(node.right)
            self.answer.append(node.val)

        travel(root)

        return self.answer

