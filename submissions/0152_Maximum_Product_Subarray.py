class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = currMax = 1
        answer = nums[0]
        for num in nums:
            vals = [num, num * currMin, num * currMax]
            currMax = max(vals)
            currMin = min(vals)
            answer = max(answer, currMax)
        
        return answer
