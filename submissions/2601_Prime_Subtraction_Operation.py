class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def isPrime(num: int) -> bool:
            for k in range(2, int(num ** 0.5) + 1):
                if num % k == 0:
                    return False
            return True

        for i in range(len(nums)):
            if i == 0:
                thresh = nums[0]
            else:
                thresh = nums[i] - nums[i - 1]

            if thresh <= 0:
                return False

            prime = 0
            for j in range(thresh - 1, 1, -1):
                if isPrime(j):
                    prime = j
                    break
            
            nums[i] = nums[i] - prime
        
        return True

