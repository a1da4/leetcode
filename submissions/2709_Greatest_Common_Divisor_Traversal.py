class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        V = set(nums)
        if 1 in V:
            return False

        nums = sorted(V, reverse=True)
        N = len(nums)
        if N == 1:
            return True
        
        for i in range(N - 1):
            for j in range(i + 1, N):
                if gcd(nums[i], nums[j]) > 1:
                    nums[j] *= nums[i]
                    break
            else:
                return False
        return True
