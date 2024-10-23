# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        prevSum = root.val
        while queue:
            n = len(queue)
            currSum = 0
            for _ in range(n):
                node = queue.popleft()
                node.val = prevSum - node.val
                sibSum = 0
                if node.left:
                    sibSum += node.left.val
                if node.right:
                    sibSum += node.right.val
                
                if node.left:
                    currSum += node.left.val
                    node.left.val = sibSum
                    queue.append(node.left)
                if node.right:
                    currSum += node.right.val
                    node.right.val = sibSum
                    queue.append(node.right)
            prevSum = currSum
        
        return root

