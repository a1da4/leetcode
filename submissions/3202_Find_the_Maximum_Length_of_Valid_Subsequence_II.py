class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        nums = [num % k for num in nums]
        num2freq = Counter(nums)

        def countAB(a: int, b: int) -> int:
            count = 0
            for num in nums:
                if count % 2 and num == a:
                    count += 1
                elif count % 2 == 0 and num == b:
                    count += 1
            
            return count
        
        answer = 0
        for a in range(k):
            for b in range(k):
                if num2freq[a] + num2freq[b] < answer:
                    continue
                answer = max(
                    answer,
                    countAB(a, b),
                )

        return answer

