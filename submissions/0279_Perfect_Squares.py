class Solution:
    def numSquares(self, n: int) -> int:
        if math.sqrt(n) % 1 == 0:
            return 1
        

        perfectSquares = [num**2 for num in range(1, 10**2+1)]

        minSquares = [n for _ in range(n + 1)]
        minSquares[0] = 0
        
        for currNum in range(n + 1):
            for perfectSquare in perfectSquares:
                if perfectSquare <= currNum:
                    minSquares[currNum] = min(minSquares[currNum], minSquares[currNum - perfectSquare] + 1)

        return minSquares[n]
