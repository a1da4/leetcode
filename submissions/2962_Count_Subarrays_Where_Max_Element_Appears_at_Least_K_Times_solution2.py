class Solution:
    def countSubarrays(
        self, 
        nums: List[int], 
        k: int,
    ) -> int:
        answer = 0
        currCount = 0
        right = 0
        N = len(nums)
        maxNum = max(nums)

        for left in range(N):
            while right < N and currCount < k:
                if nums[right] == maxNum:
                    currCount += 1
                right += 1
            
            if currCount >= k:
                answer += (N - right) + 1
            
            if nums[left] == maxNum:
                currCount -= 1

        return answer

