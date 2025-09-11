class Solution:
    def sortVowels(self, s: str) -> str:
        t = [""] * len(s)
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        queue = deque([])
        heap = []
        for i, ch in enumerate(s):
            if ch in vowels:
                heapq.heappush(heap, ch)
                queue.append(i)
            else:
                t[i] = ch
        
        while queue:
            t[queue.popleft()] = heapq.heappop(heap)

        return "".join(t)
