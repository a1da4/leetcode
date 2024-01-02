class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        nums = deque(nums)
        while nums:
            row = []
            vocab = set()
            N = len(nums)
            for _ in range(N):
                num = nums.popleft()
                if num in vocab:
                    nums.append(num)
                    continue
                else:
                    row.append(num)
                    vocab.add(num)
            answer.append(row)
        return answer
