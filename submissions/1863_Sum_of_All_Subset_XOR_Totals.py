class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.answer = 0

        def multipleXor(curr, currId, times):
            for nextId in range(currId + 1, len(nums)):
                curr ^= nums[nextId]
                self.answer += curr
                if times < len(nums):
                    multipleXor(curr, nextId, times + 1)
                curr ^= nums[nextId]

        multipleXor(0, -1, 0)
        return self.answer

