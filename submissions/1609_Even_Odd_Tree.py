# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        currStatus = 1
        nodes = deque([root])
        while nodes:
            N = len(nodes)
            prevVal = float('inf')
            if currStatus%2:
                prevVal *= -1
            for _ in range(N):
                node = nodes.popleft()
                if currStatus%2 != node.val%2:
                    return False
                if currStatus%2:
                    if prevVal >= node.val:
                        return False
                else:
                    if prevVal <= node.val:
                        return False
                prevVal = node.val

                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            currStatus += 1
        return True
