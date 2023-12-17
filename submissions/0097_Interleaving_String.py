class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        nums1 = len(s1)
        nums2 = len(s2)
        nums3 = len(s3)
        
        if nums1 + nums2 != nums3 or Counter(s1) + Counter(s2) != Counter(s3):
            return False
        
        if nums1 < nums2:
            return self.isInterleave(s2, s1, s3)
        
        dp = [False] * (nums2 + 1)
        dp[0] = True
        
        for j in range(1, nums2 + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, nums1 + 1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, nums2 + 1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])

        return dp[-1]
