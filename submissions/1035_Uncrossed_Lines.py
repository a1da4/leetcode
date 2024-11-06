class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * n2 for _ in range(n1)]

        for i in range(n1):
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1] if i > 0 and j > 0 else 1
                else:
                    dp[i][j] = max(dp[i - 1][j] if i > 0 else 0,
                                   dp[i][j - 1] if j > 0 else 0)

        return dp[-1][-1]

