class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        currId = 0
        answer = 0

        for ch in word:
            nextId = keyboard.index(ch)
            answer += abs(nextId - currId)
            currId = nextId

        return answer

