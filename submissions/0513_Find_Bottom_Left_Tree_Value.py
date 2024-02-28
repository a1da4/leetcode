# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        nodes = deque([root])
        while nodes:
            N = len(nodes)
            answer = None
            for _ in range(N):
                node = nodes.popleft()
                if answer is None:
                    answer = node.val
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
        return answer
