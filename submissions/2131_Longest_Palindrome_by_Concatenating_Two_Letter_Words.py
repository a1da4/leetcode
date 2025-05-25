class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word2freq = Counter(words)
        used_uniq = False
        answer = 0
        for word in list(set(words)):
            _word = word[::-1]
            if word not in word2freq or _word not in word2freq:
                continue

            if word == _word:
                freq = word2freq[word]
                if freq > 1:
                    answer += 2 * (freq - freq % 2)
                if freq % 2 and not used_uniq:
                    answer += 2
                    used_uniq = True
                del word2freq[word]
            
            else:
                freq, _freq = word2freq[word], word2freq[_word]
                answer += 4 * min(freq, _freq)
                del word2freq[word], word2freq[_word]
                
        return answer

