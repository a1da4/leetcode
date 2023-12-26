class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]] + [[num] for num in nums]
        for n in range(2, len(nums)+1):
            answer = answer + [list(comb) for comb in combinations(nums, n)]
        
        return answer
