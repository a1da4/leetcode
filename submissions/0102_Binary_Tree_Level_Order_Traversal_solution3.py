# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if root:
            nodes = deque([root])
            while nodes:
                N = len(nodes)
                currLevel = []
                for _ in range(N):
                    node = nodes.popleft()
                    currLevel.append(node.val)
                    if node.left:
                        nodes.append(node.left)
                    if node.right:
                        nodes.append(node.right)
                answer.append(currLevel)
        return answer
