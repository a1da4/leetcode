class Solution:
    def findEvenNumbers(
        self, 
        digits: List[int],
    ) -> List[int]:
        answer = []
        digit2freq = Counter(digits)

        for num in range(100, 1000, 2):
            _digit2freq = Counter([
                int(digit)
                for digit in str(num)
            ])

            verified = True
            for digit, freq in _digit2freq.items():
                if digit2freq[digit] < freq:
                    verified = False
                    break
            if verified:
                answer.append(num)

        return answer

