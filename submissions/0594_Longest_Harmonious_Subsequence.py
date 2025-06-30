class Solution:
    def findLHS(self, nums: List[int]) -> int:
        answer = 0
        num2freq = Counter(nums)

        for num in sorted(nums):
            if num + 1 not in num2freq:
                continue
            
            answer = max(answer, 
                num2freq[num] + num2freq[num + 1])

        return answer

