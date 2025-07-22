class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        answer = 0
        leftId = 0
        currSum = 0
        vocab = set()
        for rightId, num in enumerate(nums):
            currSum += num
            if num not in vocab:
                vocab.add(num)
                answer = max(answer, currSum)
            else:
                while leftId < rightId:
                    currSum -= nums[leftId]
                    if nums[leftId] == num:
                        leftId += 1
                        break
                    vocab.remove(nums[leftId])
                    leftId += 1

        return answer

