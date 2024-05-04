class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if Counter(s) == Counter(goal):
            diff = 0
            for _s, _g in zip(s, goal):
                if _s != _g:
                    diff += 1
            if diff == 2:
                return True
            elif diff == 0:
                return Counter(s).most_common(1)[0][1] > 1
            else:
                return False
        return False
