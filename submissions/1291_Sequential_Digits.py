class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        def makeDigits(w: int) -> List[int]:
            digits = "123456789"
            return [int(digits[i:i+w]) for i in range(9-w+1)]

        wLow = min(int(log10(low)) + 1, 9)
        wHigh = min(int(log10(high)) + 1, 9)

        answer = []
        for w in range(wLow, wHigh + 1):
            for digit in makeDigits(w):
                if low <= digit <= high:
                    answer.append(digit)

        return answer
