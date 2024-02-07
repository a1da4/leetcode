class Solution:
    def frequencySort(self, s: str) -> str:
        c2f = Counter(s)
        answer = ""
        for char, freq in c2f.most_common():
            answer += char * freq

        return answer
