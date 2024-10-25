class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        length = [1] * N
        count = [1] * N
        
        for i in range(N):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0        
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
                            
        maxLen = max(length)
        answer = 0

        for i in range(N):
            if length[i] == maxLen:
                answer += count[i]
        
        return answer
    
