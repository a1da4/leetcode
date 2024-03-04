class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        def faceUp(power, score, token):
            if power >= token:
                power -= token
                score += 1
            return power, score

        def faceDown(power, score, token):
            if score >= 1:
                power += token
                score -= 1
            return power, score
        
        score = 0
        maxScore = 0
        tokens = deque(sorted(tokens))
        while tokens:
            if len(tokens) >= 2:
                headToken = tokens.popleft()
                tailToken = tokens.pop()
                is_continue = True
            else:
                headToken = tailToken = tokens.pop()
                is_continue = False
            if score == 0 or power >= headToken:
                power, score = faceUp(power, score, headToken)
                maxScore = max(maxScore, score)
                if is_continue:
                    tokens.append(tailToken)
            else:
                power, score = faceDown(power, score, tailToken)
                if is_continue:
                    tokens.appendleft(headToken)

        return maxScore
