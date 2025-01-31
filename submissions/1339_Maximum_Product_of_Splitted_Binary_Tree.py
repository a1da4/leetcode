# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []

        def search(root):
            if root is None:
                return 0
            left = search(root.left)
            right = search(root.right)
            total = left + right + root.val
            sums.append(total)

            return total
        
        total = search(root)
        answer = 0
        for curr in sums:
            answer = max(answer, curr * (total - curr))
        
        return answer % (10 ** 9 + 7)

