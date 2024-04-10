class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        answer = []
        deck.sort()
        answer.append(deck.pop())
        while deck:
            num_i = deck.pop()
            num_j = answer.pop()
            answer = [num_i] + [num_j] + answer
        return answer

