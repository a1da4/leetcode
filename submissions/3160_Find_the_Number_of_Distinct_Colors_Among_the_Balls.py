class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        answer = []
        color2freq = {}
        ball2color = {}
        for query in queries:
            ball, color = query
            if ball in ball2color:
                prev = ball2color[ball]
                color2freq[prev] -= 1
                if color2freq[prev] == 0:
                    del color2freq[prev]

            ball2color[ball] = color
            if color not in color2freq:
                color2freq[color] = 0
            color2freq[color] += 1

            answer.append(len(color2freq))

        return answer

