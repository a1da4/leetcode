# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        self.vals = []

        def addLeaves(node: Optional[TreeNode]):
            if not node.left and not node.right:
                self.vals.append(node.val)
            else:
                if node.left:
                    addLeaves(node.left)
                if node.right:
                    addLeaves(node.right)

        if not root:
            return
        if root.left or root.right:
            self.vals.append(root.val)
        leftNode = root.left
        while leftNode:
            if leftNode.left or leftNode.right:
                self.vals.append(leftNode.val)
            if leftNode.left:
                leftNode = leftNode.left
            else:
                leftNode = leftNode.right
        addLeaves(root)

        stack = []

        rightNode = root.right
        while rightNode:
            if rightNode.left or rightNode.right:
                stack.append(rightNode.val)
            if rightNode.right:
                rightNode = rightNode.right
            else:
                rightNode = rightNode.left
        
        while stack:
            self.vals.append(stack.pop())

        return self.vals

