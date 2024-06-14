# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        else:
            self.dir2vals = {0: []}

            queue = deque([(root, 0)])
            while queue:
                node, currDir = queue.popleft()
                if node:
                    if currDir in self.dir2vals:
                        self.dir2vals[currDir].append(node.val)
                    else:
                        self.dir2vals[currDir] = [node.val]
                    queue.append((node.left, currDir - 1))
                    queue.append((node.right, currDir + 1))

            return [self.dir2vals[_dir] for _dir in sorted(self.dir2vals.keys())]

