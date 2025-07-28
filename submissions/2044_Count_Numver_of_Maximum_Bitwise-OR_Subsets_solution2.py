class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = 0
        for num in nums:
            target |= num
        
        @lru_cache(maxsize=None)
        def dfs(currId: int, currOr: int) -> int:
            if currId == len(nums):
                return 1 if currOr == target else 0
            
            added = dfs(currId + 1, currOr | nums[currId])
            ignored = dfs(currId + 1, currOr)

            return added + ignored

        return dfs(0, 0)
