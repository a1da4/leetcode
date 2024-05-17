# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def getDepth(node: Optional[TreeNode]) -> int:
            depth = 1
            queue = deque([node])
            while queue:
                N = len(queue)
                depth += 1
                for _ in range(N):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return depth

        def isLeaf(node: Optional[TreeNode]) -> bool:
            return node.left == node.right == None

        def delNext(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node.left is None:
                pass
            elif isLeaf(node.left) and node.left.val == target:
                node.left = None
            else:
                node.left = delNext(node.left)

            if node.right is None:
                pass
            elif isLeaf(node.right) and node.right.val == target:
                node.right = None
            else:
                node.right = delNext(node.right)
            return node

        depth = getDepth(root)
        for _ in range(depth):
            root = delNext(root)
        if isLeaf(root) and root.val == target:
            root = None
        return root

