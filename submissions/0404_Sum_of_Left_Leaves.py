# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        nodes = deque([(root, False)])
        while nodes:
            N = len(nodes)
            for _ in range(N):
                node, is_left = nodes.popleft()
                if is_left and node.left is None and node.right is None:
                    self.answer += node.val
                
                if node.left:
                    nodes.append([node.left, True])
                if node.right:
                    nodes.append([node.right, False])

        return self.answer
