class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = ""
        spaces = set(spaces)
        for i, ch in enumerate(s):
            if i in spaces:
                answer += " "
            answer += ch

        return answer

