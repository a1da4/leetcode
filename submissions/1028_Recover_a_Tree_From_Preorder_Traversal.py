# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        N = len(traversal)
        currId = 0
        item = ""
        while currId < N and traversal[currId] != "-":
            item += traversal[currId]
            currId += 1
        
        root = TreeNode(int(item))
        curr = root
        stack = [root]
        prevLevel = -1
        
        while currId < N:
            level = 0
            item = ""
            while traversal[currId] == "-":
                level += 1
                currId += 1
            while currId < N and traversal[currId] != "-":
                item += traversal[currId]
                currId += 1
            num = int(item)
            
            if prevLevel < level:
                curr.left = TreeNode(num)
                curr = curr.left
            else:
                if len(stack) > level:
                    stack = stack[:level]
                node = stack[-1]
                node.right = TreeNode(num)
                curr = node.right
            
            stack.append(curr)
            prevLevel = level

        return root

