# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        nodes = deque([root])
        while nodes:
            currNode = nodes.pop()

            if currNode.right:
                nodes.append(currNode.right)
            if currNode.left:
                nodes.append(currNode.left)
    
            if nodes:
                currNode.right = nodes.pop()
                nodes.append(currNode.right)
            currNode.left = None

