class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ch2freqs_ref = [Counter(word2) for word2 in list(set(words2))]
        ch2freq_ref = {}
        for ch2freq in ch2freqs_ref:
            for ch, freq in ch2freq.items():
                if ch not in ch2freq_ref or ch2freq_ref[ch] < freq:
                    ch2freq_ref[ch] = freq

        answer = []
        for word1 in words1:
            ch2freq_tar = Counter(word1)

            for ch, freq in ch2freq_ref.items():
                if ch not in ch2freq_tar or ch2freq_tar[ch] < freq:
                    break
            else:
                answer.append(word1)

        return answer

