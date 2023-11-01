# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftNodes = [root]
        rightNodes = [root]

        while leftNodes and rightNodes:
            numNodes = len(leftNodes)
            for _ in range(numNodes):
                leftNode = leftNodes.pop(0)
                rightNode = rightNodes.pop(0)

                if leftNode.left is None and rightNode.right is None:
                    pass
                elif leftNode.left is None or rightNode.right is None:
                    return False
                elif leftNode.left.val == rightNode.right.val: 
                    leftNodes.append(leftNode.left)
                    rightNodes.append(rightNode.right)
                else:
                    return False

                if leftNode.right is None and rightNode.left is None:
                    pass
                elif leftNode.right is None or rightNode.left is None:
                    return False
                elif leftNode.right.val == rightNode.left.val:
                    leftNodes.append(leftNode.right)
                    rightNodes.append(rightNode.left)
                else:
                    return False
        
        return True
