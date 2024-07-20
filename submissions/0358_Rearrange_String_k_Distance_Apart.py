class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        ch2freq = Counter(s)
        maxFreq = ch2freq.most_common(1)[0][1]
        mostChars = []
        secondChars = []
        for ch, freq in ch2freq.most_common():
            if freq == maxFreq:
                mostChars.append(ch)
            elif freq == maxFreq - 1:
                secondChars.append(ch)
            else:
                break
        
        segments = [""] * maxFreq
        for freqId in range(maxFreq - 1):
            segments[freqId] += ''.join(mostChars) \
                               + ''.join(secondChars)
        segments[-1] += ''.join(mostChars)

        most_second_ch = set(segments[0])

        freqId = 0
        for ch, freq in ch2freq.items():
            if ch in most_second_ch:
                continue
            for _ in range(freq):
                segments[freqId] += ch
                freqId = (freqId + 1) % (maxFreq - 1)
        
        for segment in segments[:-1]:
            if len(segment) < k:
                return ''

        return ''.join(segments)

