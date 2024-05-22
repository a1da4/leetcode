class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []

        def search(s, path):
            if not s:
                answer.append(path)
                return
            for currId in range(1, len(s) + 1):
                if s[:currId] == s[:currId][::-1]:
                    search(s[currId:], path + [s[:currId]])
        
        search(s, [])

        return answer
