class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = set()
        nums.sort()
        for leftId in range(len(nums)):
            if leftId >= len(nums) - 2:
                continue
            
            centerId = leftId + 1
            rightId = len(nums) - 1
            while leftId < centerId < rightId:
                leftNum = nums[leftId]
                centerNum = nums[centerId]
                rightNum = nums[rightId]
                
                currSum = leftNum + centerNum + rightNum
                if currSum < 0:
                    centerId += 1
                elif currSum > 0:
                    rightId -= 1
                else:
                    answers.add((leftNum, centerNum, rightNum))
                    centerId += 1
                    rightId -= 1

        return answersclass Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = set()
        nums.sort()
        for leftId in range(len(nums)):
            if leftId >= len(nums) - 2:
                continue
            
            centerId = leftId + 1
            rightId = len(nums) - 1
            while leftId < centerId < rightId:
                leftNum = nums[leftId]
                centerNum = nums[centerId]
                rightNum = nums[rightId]
                
                currSum = leftNum + centerNum + rightNum
                if currSum < 0:
                    centerId += 1
                elif currSum > 0:
                    rightId -= 1
                else:
                    answers.add((leftNum, centerNum, rightNum))
                    centerId += 1
                    rightId -= 1

        return answers
