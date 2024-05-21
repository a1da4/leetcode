class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.answer = [[]]

        def combinations(currNums: List[int], currId: int):
            for nextId in range(currId + 1, len(nums)):
                currNums.append(nums[nextId])
                self.answer.append(currNums[:])
                combinations(currNums, nextId)
                currNums.remove(nums[nextId])

        combinations([], -1)
        return self.answer

