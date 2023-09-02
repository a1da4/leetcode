class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        answer = 0
        while a or b or c:
            if c & 1:
                if ((a & 1) or (b & 1)):
                    pass
                else:
                    answer += 1
            else:
                answer += ((a & 1) + (b & 1))
            
            a >>= 1
            b >>= 1
            c >>= 1
        
        return answer
