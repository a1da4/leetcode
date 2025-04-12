class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        kPalindromes = [
            palindrome 
            for palindrome in self.generateNdigitPalindromes(n)
            if palindrome % k == 0
        ]
        answer = 0
        vocab = set()
        for palindrome in kPalindromes:
            key = self.convertPalindromeIntoKey(palindrome)
            if key in vocab:
                continue
            
            vocab.add(key)
            answer += self.countFromKey(n, key)

        return answer

    def generateNdigitPalindromes(self, n: int) -> List[int]:
        if n % 2:
            palindromes = [str(d) for d in range(10)]
            n -= 1
        else:
            palindromes = [""]

        n //= 2

        for i in range(n):
            nextPalindromes = []
            for palindrome in palindromes:
                for d in range(10):
                    if d == 0 and i == n - 1:
                        continue
                    nextPalindromes.append(
                        str(d) + palindrome + str(d)
                    )
            palindromes = nextPalindromes

        return [int(p) for p in palindromes]

    def convertPalindromeIntoKey(self, palindrome: int) -> str:
        digit2freq = Counter(str(palindrome))
        palindrome_keys = [] 

        for key in sorted(digit2freq.keys()):
            val = digit2freq[key]
            palindrome_keys.append(f"{key}-{str(val)}")

        return "_".join(palindrome_keys)

    def countFromKey(self, n: int, palindrome_key: str) -> int:
        count = math.perm(n)
        count_ignore_zero = math.perm(n - 1)
        contains_zero = False

        for digit_freq in palindrome_key.split("_"):
            digit, freq = digit_freq.split("-")
            digit, freq = int(digit), int(freq)
            
            count //= math.perm(freq)
            if digit == 0:
                count_ignore_zero //= math.perm(freq - 1)
                contains_zero = True
            else:
                count_ignore_zero //= math.perm(freq)

        return count - count_ignore_zero if contains_zero else count

