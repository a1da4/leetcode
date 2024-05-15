class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        numOdds = 0
        N = len(s)
        for val in Counter(s).values():
            if val % 2:
                numOdds += 1
                if numOdds > N%2:
                    return False

        return True
