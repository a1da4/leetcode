class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num2id = {}
        for numId, num in enumerate(numbers):
            if target - num in num2id:
                # target-num < num
                return [num2id[target-num]+1, numId+1]
            num2id[num] = numId
