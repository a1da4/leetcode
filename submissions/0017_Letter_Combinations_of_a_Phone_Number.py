class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        def addChar(digit: str, answer: List[str], letterVocab: Set[str]) -> Tuple[List[str], Set[str]]:
            digit2letters = {"2": ["a", "b", "c"],
                           "3": ["d", "e", "f"],
                           "4": ["g", "h", "i"],
                           "5": ["j", "k", "l"],
                           "6": ["m", "n", "o"],
                           "7": ["p", "q", "r", "s"],
                           "8": ["t", "u", "v"],
                           "9": ["w", "x", "y", "z"]}
            letters = digit2letters[digit]
            numAnswer = len(answer)
            if numAnswer == 0:
                for letter in letters:
                    answer.append(letter)
                    letterVocab.add(letter)
            else:
                for _ in range(numAnswer):
                    each = answer.pop(0)
                    for letter in letters:
                        if each + letter not in letterVocab:
                            answer.append(each + letter)
                            letterVocab.add(each + letter)
            return answer, letterVocab
        
        answer = []
        letterVocab = set()
        for digit in digits:
            answer, letterVocab = addChar(digit, answer, letterVocab)
        
        return answer
