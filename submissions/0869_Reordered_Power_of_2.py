class Solution:
    def countDigit(self, n: int) -> bool:
        return math.floor(math.log10(n))
    
    def convertStr(self, n: int) -> str:
        return ''.join(
            sorted(
                [ch for ch in str(n)]
            )
        )

    def reorderedPowerOf2(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            n_digit = self.countDigit(n)
            vocab = set()
            curr = 2
            while self.countDigit(curr) < n_digit:
                curr *= 2
            
            while self.countDigit(curr) == n_digit:
                vocab.add(self.convertStr(curr))
                curr *= 2
        
        return self.convertStr(n) in vocab
