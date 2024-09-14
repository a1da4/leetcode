class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxNum = 0
        answer = 0
        curr = 0

        for num in nums:
            if maxNum < num:
                maxNum = num
                answer = 0
                curr = 0

            if maxNum == num:
                curr += 1
            else:
                curr = 0
            
            answer = max(answer, curr)
        
        return answer


