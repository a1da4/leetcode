class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        answer = 0
        N = len(nums)
        nums = deque(nums)

        while N > 0 and len(set(nums)) != N:
            answer += 1

            if N <= 3:
                N = 0
            else:
                N -= 3
                for _ in range(3):
                    nums.popleft()

        return answer

