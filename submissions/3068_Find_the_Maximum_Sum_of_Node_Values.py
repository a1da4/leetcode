class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        N = len(nums)
        memo = [[-1] * 2 for _ in range(N)]

        def _helper(currId: int, isEven: int, memo: List[List[int]]):
            if currId == N:
                return 0 if isEven == 1 else -float('inf')
            if memo[currId][isEven] != -1:
                return memo[currId][isEven]
            woXor = nums[currId] + _helper(currId + 1, isEven, memo)
            wXor = (nums[currId] ^ k) + _helper(currId + 1, 1 - isEven, memo)
            memo[currId][isEven] = max(woXor, wXor)
            return memo[currId][isEven]

        return _helper(0, 1, memo)

