# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def search(node: Optional[TreeNode], result: List[List[int]], depth=0):
            if not node:
                return
            
            if len(result) < depth+1:
                result.append([])
            
            result[depth].append(node.val)
            
            if node.left:
                search(node.left, result, depth+1)
            if node.right:
                search(node.right, result, depth+1)
            return result
        
        return search(root, [], 0)
