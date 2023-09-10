class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        maxElement = 0
        currElement = 0
        answer = nums[0]
        currNum = nums[0]
        for num in nums:
            if num == currNum:
                currElement += 1
            else:
                if currElement > maxElement:
                    maxElement = currElement
                    answer = currNum
                currNum = num
                currElement = 1

        if currElement > maxElement:
            maxElement = currElement
            answer = currNum

        return answer
