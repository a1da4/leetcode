class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        founds = set()
        for num in nums:
            if num in founds:
                answer.append(num)
            else:
                founds.add(num)
        return answer
