# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            depth = []
            depth_size = len(queue)

            if len(result) % 2 != 0:
                queue = queue[::-1]
                cache = []

            for current_depth in range(depth_size):
                node = queue.pop(0)
                depth.append(node.val)
                
                if len(result) % 2 == 0:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    cache.append(node)
            
            if len(result) % 2 != 0:
                cache = cache[::-1]
                for node in cache:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            
            result.append(depth)
        
        return result
