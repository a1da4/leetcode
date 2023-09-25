class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def initialize(word) -> Tuple[List[str], int]:
            currWords = [word]
            currLength = len(word)
            return currWords, currLength

        def justifyLeft(currWords: List[str], currLength: int, maxLength: int) -> str:
            currWords[-1] += " " * (maxLength - currLength)
            return " ".join(currWords)

        def justifyFully(currWords: List[str], currLength: int, maxLength: int) -> str:
            currId = 0
            maxId = len(currWords)
            while currLength < maxLength:
                if currId < maxId - 1:
                    currWords[currId] += " "
                    currLength += 1
                currId = (currId + 1) % maxId
            return " ".join(currWords)

        def update(currWords: List[str], currLength: int, maxLength: int, answer: List[List[str]]) -> List[List[str]]:
            if len(currWords) == 1:
                # len(currWords) == 1 -> left-justified
                justified = justifyLeft(currWords, currLength, maxLength)
            else:    
                # len(currWords) > 1 -> fully-justified
                justified = justifyFully(currWords, currLength, maxLength)
            answer.append(justified)
            return answer


        answer = []
        currWords, currLength = initialize(words[0])
        for word in words[1:]:
            length = len(word)
            if currLength + length + 1 <= maxWidth:
                currWords.append(word)
                currLength += length + 1
            else:
                answer = update(currWords, currLength, maxWidth, answer)
                currWords, currLength = initialize(word)
        
        if currWords is not None:
            justified = justifyLeft(currWords, currLength, maxWidth)
            answer.append(justified)
        
        return answer
