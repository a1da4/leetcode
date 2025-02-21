# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.root = root
        self.vals = {0}
        queue = deque([root])

        while queue:
            N = len(queue)
            for _ in range(N):
                node = queue.popleft()
                if node.left:
                    val = 2 * node.val + 1
                    self.vals.add(val)
                    node.left.val = val
                    queue.append(node.left)
                if node.right:
                    val = 2 * node.val + 2
                    self.vals.add(val)
                    node.right.val = val
                    queue.append(node.right)

    def find(self, target: int) -> bool:
        return target in self.vals

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
