from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        answer.append([])
        for subLength in range(1, len(nums)):
            for pairNums in combinations(nums, subLength):
                answer.append(pairNums)
        
        answer.append(nums)

        return answer
