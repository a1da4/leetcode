class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        w2f = Counter(arr)
        w2f_sorted = deque(w2f.most_common()[::-1])
        answer = len(w2f)
        while k > 0:
            key, val = w2f_sorted.popleft()
            if val > k:
                k = 0
            else:
                k -= val
                answer -= 1
        
        return answer
