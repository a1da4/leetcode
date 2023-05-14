# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def recursiveCreation(currentTree, preorder, inorder):
            if len(preorder) == 0:
                return currentTree

            rootNode = preorder[0]
            preorder.pop(0)

            currentTree.val = rootNode

            rootIndex = inorder.index(rootNode)
            leftSubtree = inorder[:rootIndex]
            rightSubtree = inorder[rootIndex+1:]

            if len(leftSubtree) > 0:
                currentTree.left = recursiveCreation(TreeNode(), preorder, leftSubtree)
            
            if len(rightSubtree) > 0:
                currentTree.right = recursiveCreation(TreeNode(), preorder, rightSubtree)

            return currentTree

        return recursiveCreation(TreeNode(), preorder, inorder)
