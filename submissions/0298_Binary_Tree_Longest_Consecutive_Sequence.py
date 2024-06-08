# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        def dfs(node, currSeq, maxSeq) -> int:
            if not node.left and not node.right:
                return maxSeq
            if node.left:
                if node.val + 1 == node.left.val:
                    seq_left = dfs(node.left, currSeq + 1, max(maxSeq, currSeq + 1))
                else:
                    seq_left = dfs(node.left, 1, max(maxSeq, currSeq))
            else:
                seq_left = maxSeq

            if node.right:
                if node.val + 1 == node.right.val:
                    seq_right = dfs(node.right, currSeq + 1, max(maxSeq, currSeq + 1))
                else:
                    seq_right = dfs(node.right, 1, max(maxSeq, currSeq))
            else:
                seq_right = maxSeq

            return max(seq_left, seq_right)

        return dfs(root, 1, 1)
