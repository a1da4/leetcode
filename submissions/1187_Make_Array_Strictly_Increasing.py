class Solution:
    def makeArrayIncreasing(
        self, 
        arr1: List[int], 
        arr2: List[int],
    ) -> int:

        dp = {-1: 0}
        arr2.sort()
        N1, N2 = len(arr1), len(arr2)
        
        for i in range(N1):
            newDp = collections.defaultdict(lambda: float('inf'))
            for prev in dp:
                if arr1[i] > prev:
                    newDp[arr1[i]] = min(newDp[arr1[i]], dp[prev])
                j = bisect.bisect_right(arr2, prev)
                if j < N2:
                    newDp[arr2[j]] = min(newDp[arr2[j]], 1 + dp[prev])
            dp = newDp

        return min(dp.values()) if dp else -1
