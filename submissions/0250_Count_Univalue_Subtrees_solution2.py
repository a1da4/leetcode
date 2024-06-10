# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:   
        self.answer = 0
        
        def dfs(node: Optional[TreeNode]) -> bool:
            if node is None:
                return True
            is_left_uni = dfs(node.left)
            is_right_uni = dfs(node.right)

            if is_left_uni and is_right_uni:
                if node.left and node.left.val != node.val:
                    return False
                if node.right and node.right.val != node.val:
                    return False
                self.answer += 1
                return True
            return False

        dfs(root)
        return self.answer

