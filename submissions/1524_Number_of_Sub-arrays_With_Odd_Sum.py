class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        count = {0: 1, 1: 0}
        answer = 0
        currSum = 0
        
        for num in arr:
            currSum += num
            binary = currSum % 2
            answer = (answer + count[1 - binary]) % MOD
            count[binary] += 1
        
        return answer

