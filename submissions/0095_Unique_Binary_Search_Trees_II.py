class Solution:
    def allPossibleBST(self, start, end):
        res = []
        if start > end:
            res.append(None)
            return res
        if (start, end) in self.memo:
            return self.memo[(start, end)]

        for i in range(start, end + 1):
            leftSubTrees = self.allPossibleBST(start, i - 1)
            rightSubTrees = self.allPossibleBST(i + 1, end)

            for left in leftSubTrees:
                for right in rightSubTrees:
                    root = TreeNode(i, left, right)
                    res.append(root)

        self.memo[(start, end)] = res
        return res

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self.memo = {}

        return self.allPossibleBST(1, n)

