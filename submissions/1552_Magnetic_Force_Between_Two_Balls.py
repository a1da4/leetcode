class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        N = len(position)
        answer = 0

        def verify(x):
            prev = position[0]
            numBalls = 1
            for curr in position[1:]:
                if curr - prev >= x:
                    numBalls += 1
                    prev = curr
                if numBalls == m:
                    return True
            return False

        low = 1
        high = int(position[-1] / (m - 1)) + 1
        while low <= high:
            mid = low + (high - low) // 2
            if verify(mid):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return answer
    
