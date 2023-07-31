# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        answer = []
        currentNodes = deque()
        currentNodes.append(root)

        while currentNodes:
            numNodes = len(currentNodes)
            for i in range(numNodes):
                temp = deque()
                currentNode = currentNodes.popleft()
                temp.append(currentNode.val)
                
                if currentNode.left:
                    currentNodes.append(currentNode.left)
                if currentNode.right:
                    currentNodes.append(currentNode.right)
            answer.append(temp.pop())

        return answer
