class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        max_number = 0
        for num in nums:
            points[num] += num
            max_number = max(max_number, num)

        self.memo = {0: 0, 1: points[1]}

        def max_points(num):
            if num not in self.memo:            
                self.memo[num] = max(max_points(num - 1), 
                    max_points(num - 2) + points[num])
            
            return self.memo[num]
        
        return max_points(max_number)

