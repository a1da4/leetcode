class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def isPrefixAndSuffix(str1: str, str2: str) -> bool:
            if len(str1) > len(str2):
                return False
            n = len(str1)
            return str2[:n] == str1 and str2[-n:] == str1

        answer = 0     
        N = len(words)   
        for i in range(N):
            for j in range(i + 1, N):
                if isPrefixAndSuffix(words[i], words[j]):
                    answer += 1
        
        return answer

