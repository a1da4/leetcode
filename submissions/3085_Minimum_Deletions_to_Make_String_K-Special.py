class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        answer = len(word)

        freqs = Counter(word).values()
        if max(freqs) - min(freqs) <= k:
            return 0
        
        for leftFreq in sorted(set(freqs)):
            rightFreq = leftFreq + k
            deletion = 0
            for freq in freqs:
                if freq < leftFreq:
                    deletion += freq
                elif freq > rightFreq:
                    deletion += freq - rightFreq
            
            answer = min(answer, deletion)

        return answer
