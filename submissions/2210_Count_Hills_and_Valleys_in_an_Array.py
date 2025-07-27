class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        answer = 0
        N = len(nums)
        prevNum, prevState = None, 0
        for i in range(1, N):
            if nums[i] == prevNum:
                currState = prevState
            else:
                left = -1
                for j in range(i - 1, -1, -1):
                    if nums[j] != nums[i]:
                        left = j
                        break
                right = -1
                for j in range(i + 1, N):
                    if nums[j] != nums[i]:
                        right = j
                        break

                if ((left >= 0 and right >= 0)
                and (
                    (nums[i] < nums[left] and nums[i] < nums[right])
                    or
                    (nums[i] > nums[left] and nums[i] > nums[right])
                )):
                    currState = 1
                else:
                    currState = 0
            
                answer += currState
            prevNum = nums[i]
            prevState = currState

        return answer

