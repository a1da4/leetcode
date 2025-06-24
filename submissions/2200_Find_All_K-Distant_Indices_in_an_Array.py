class Solution:
    def findKDistantIndices(
        self, 
        nums: List[int], 
        key: int, 
        k: int,
    ) -> List[int]:
        answer = set()

        N = len(nums)
        for j, num in enumerate(nums):
            if num == key:
                for i in range(j - k, j + k + 1):
                    if i < 0 or i >= N:
                        continue
                    answer.add(i)

        return sorted(list(answer))
