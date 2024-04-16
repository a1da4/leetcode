# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val=val, left=root)

        currDepth = 1
        _root = root
        nodes = [_root]
        while nodes:
            N = len(nodes)
            if currDepth + 1 == depth:
                for node in nodes:
                    tempLeft = node.left
                    tempRight = node.right
                    node.left = TreeNode(val=val, left=tempLeft)
                    node.right = TreeNode(val=val, right=tempRight)
                break
            for _ in range(N):
                node = nodes.pop(0)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            currDepth += 1
        return root
