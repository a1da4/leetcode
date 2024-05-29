class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        answer = []

        for interval in intervals:
            start, end = interval
            if start >= toBeRemoved[0] and end <= toBeRemoved[1]:
                continue
            elif start < toBeRemoved[0] and toBeRemoved[1] < end:
                answer.append([start, toBeRemoved[0]])
                answer.append([toBeRemoved[1], end])
            elif start >= toBeRemoved[1] or end <= toBeRemoved[0]:
                answer.append([start, end])
            else:
                if toBeRemoved[0] <= start <= toBeRemoved[1]:
                    answer.append([toBeRemoved[1], end])
                else:
                    answer.append([start, toBeRemoved[0]])
        return answer
