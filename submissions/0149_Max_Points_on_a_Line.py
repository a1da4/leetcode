class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # grad: n(n-1)/2 patterns
        points.sort()
        numPoints = len(points)
        if numPoints == 1:
            return 1
        
        maxPatterns = 1
        
        for i in range(numPoints - 1):
            grads = []
            for j in range(i+1, numPoints):
                xGrad = points[j][0] - points[i][0]
                yGrad = points[j][1] - points[i][1]
                
                if xGrad == 0:
                    # y' = y" = b
                    grad = "y"
                elif yGrad == 0:
                    # x' = x" = b
                    grad = "x"
                else:
                    # consider 6/4 = 3/2
                    g = gcd(yGrad, xGrad)
                    yGrad //= g
                    xGrad //= g
                    grad = math.atan2(yGrad, xGrad)
                grads.append(f"{grad}")
            maxPatterns = max(maxPatterns, Counter(grads).most_common()[0][1] + 1)
        
        return maxPatterns
