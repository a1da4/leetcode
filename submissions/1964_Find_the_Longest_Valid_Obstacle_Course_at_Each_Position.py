class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        answer = []
        items = []

        for obs in obstacles:
            pos = bisect_right(items, obs)
            if pos == len(items):
                items.append(obs)
            else:
                items[pos] = obs
            answer.append(pos + 1)

        return answer

