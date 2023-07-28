# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        sum2freq = defaultdict(int)
        sum2freq[0] = 1

        def dfs(root: Optional[TreeNode], total: int) -> int:
            count = 0
            if root:
                total += root.val

                count = sum2freq[total - targetSum]
                sum2freq[total] += 1
                count += dfs(root.left, total) + dfs(root.right, total)

                sum2freq[total] -= 1
            return count
        
        return dfs(root, 0)
