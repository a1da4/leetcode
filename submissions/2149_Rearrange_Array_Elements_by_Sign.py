class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posNums = [num for num in nums if num > 0]
        negNums = [num for num in nums if num < 0]

        answer = []
        for pos, neg in zip(posNums, negNums):
            answer += [pos, neg]

        return answer
