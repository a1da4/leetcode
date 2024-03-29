class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxNum = max(nums)
        maxIds = []
        maxFreq = 0
        answer = 0
    
        for currId, num in enumerate(nums):
            if num == maxNum:
                maxIds.append(currId)
                maxFreq += 1
        
            if maxFreq >= k:
                answer += maxIds[-k] + 1
     
        return answer
