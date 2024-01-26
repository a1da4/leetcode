class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = deque([s])
        visited = set()
        while queue:
            target = queue.popleft()
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

