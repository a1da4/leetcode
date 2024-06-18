# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def getVals(root: Optional[TreeNode]) -> Set[int]:
            vals = set()
            queue = deque([root])
            while queue:
                N = len(queue)
                for _ in range(N):
                    node = queue.popleft()
                    vals.add(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            return vals
        
        vals1 = getVals(root1)
        vals2 = getVals(root2)

        for val1 in vals1:
            if target - val1 in vals2:
                return True
        
        return False

