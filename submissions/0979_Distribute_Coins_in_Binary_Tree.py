# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.answer = 0

        def search(node: Optional[TreeNode]) -> int:
            leftCoin = search(node.left) if node.left else 0
            rightCoin = search(node.right) if node.right else 0
            self.answer += abs(leftCoin) + abs(rightCoin)
            return node.val - 1 + leftCoin + rightCoin

        search(root)

        return self.answer

