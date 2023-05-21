class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = [s]
        visited = set()
        while queue:
            target = queue.pop(0)
            if target in visited:
                continue
            for word in wordDict:
                if target == word:
                    return True
                if len(target) < len(word):
                    continue
                if target[:len(word)] == word:
                    queue.append(target[len(word):])
            visited.add(target)
        
        return False
