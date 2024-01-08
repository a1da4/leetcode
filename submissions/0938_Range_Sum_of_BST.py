# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = 0
        nodes = deque([root])
        while nodes:
            N = len(nodes)
            for _ in range(N):
                node = nodes.popleft()
                if low <= node.val <= high:
                    answer += node.val
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
        return answer
