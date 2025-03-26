class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        rem = None
        for row in grid:
            for num in row:
                nums.append(num)
                if rem is None:
                    rem = num % x
                else:
                    if num % x != rem:
                        return -1
        
        nums.sort()
        N = len(nums)

        comNum = nums[N // 2]
        answer = 0
        for num in nums:
            answer += abs(comNum - num) // x

        return answer

