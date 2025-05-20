class Solution:
    def isZeroArray(
        self, 
        nums: List[int], 
        queries: List[List[int]],
    ) -> bool:  
        N = len(nums)
        _nums = [0] * (N + 1)
        for query in queries:
            _nums[query[0]] += 1
            _nums[query[1] + 1] -= 1

        _num = 0
        for i in range(N):
            _num += _nums[i]
            if nums[i] > _num:
                return False

        return True 

