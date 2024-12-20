# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        curr = 0
        while queue:
            curr += 1
            N = len(queue)
            if curr % 2 == 0:
                vals = []
                for _ in range(N):
                    node = queue.popleft()
                    vals.append(node.val)
                    queue.append(node)
                for _ in range(N):
                    node = queue.popleft()
                    node.val = vals.pop()
                    queue.append(node)

            for _ in range(N):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root

