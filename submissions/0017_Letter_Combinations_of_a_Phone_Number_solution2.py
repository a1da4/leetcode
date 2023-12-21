class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        num2letters = {"2": ["a", "b", "c"], "3": ["d", "e", "f"],
                       "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                       "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                       "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        
        chars = [""]
        for num in digits:
            numChars = len(chars)
            for _ in range(numChars):
                currChar = chars.pop(0)
                for letter in num2letters[num]:
                    chars.append(currChar + letter)
        
        return chars
