class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        def calculate(speed: int) -> float:
            time = 0.0
            for d in dist:
                time = math.ceil(time)
                time += d / speed
            return time

        l, r = 1, 10**7
        answer = -1
        while l <= r:
            m = (l + r) // 2
            t = calculate(m)
            if t <= hour:
                answer = m
                r = m - 1
            else:
                l = m + 1

        return answer
