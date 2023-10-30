# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if (p is None and q is not None) or (p is not None and q is None):
            return False

        pNodes = [p]
        qNodes = [q]

        while pNodes and qNodes:
            numNodes = len(pNodes)
            for _ in range(numNodes):
                pNode = pNodes.pop(0)
                qNode = qNodes.pop(0)

                if pNode.val != qNode.val:
                    return False

                if pNode.left and qNode.left:
                    pNodes.append(pNode.left)
                    qNodes.append(qNode.left)
                elif pNode.left is None and qNode.left is None:
                    pass
                else:
                    return False
                
                if pNode.right and qNode.right:
                    pNodes.append(pNode.right)
                    qNodes.append(qNode.right)
                elif pNode.right is None and qNode.right is None:
                    pass
                else:
                    return False

        return True
