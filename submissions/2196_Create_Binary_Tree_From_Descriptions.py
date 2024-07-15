# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        num2node = {}
        num2ischild = {}

        for description in descriptions:
            parent, child, isLeft = description
            if parent not in num2node:
                num2node[parent] = TreeNode(parent)
                num2ischild[parent] = False
            if child not in num2node:
                num2node[child] = TreeNode(child)
                num2ischild[child] = True
            if isLeft:
                num2node[parent].left = num2node[child]
                num2ischild[child] = True
            else:
                num2node[parent].right = num2node[child]
                num2ischild[child] = True

        for num in num2node.keys():
            if not num2ischild[num]:
                return num2node[num]

