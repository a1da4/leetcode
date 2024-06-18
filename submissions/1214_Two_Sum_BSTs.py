# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.visited = set()

    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        if not root1 or not root2:
            return False
        if (root1, root2) in self.visited:
            return False
        self.visited.add((root1, root2))
        if root1.val + root2.val == target:
            return True
        else:
            if root1.val + root2.val > target:
                return self.twoSumBSTs(root1.left, root2, target) \
                    or self.twoSumBSTs(root1, root2.left, target)
            else:
                return self.twoSumBSTs(root1.right, root2, target) \
                    or self.twoSumBSTs(root1, root2.right, target)
