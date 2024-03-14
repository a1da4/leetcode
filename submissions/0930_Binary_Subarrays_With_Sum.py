class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        num2freq = {0: 1}
        currSum = 0
        answer = 0
        
        for num in nums:
            currSum += num
            if currSum - goal in num2freq:
                answer += num2freq[currSum - goal]
            num2freq[currSum] = num2freq.get(currSum, 0) + 1

        return answer
