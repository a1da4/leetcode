class Solution:
    def spellchecker(
        self, 
        wordlist: List[str], 
        queries: List[str],
    ) -> List[str]:
        words = set(wordlist)
        vowels = {
            'a', 'e', 'i', 'o', 'u',
            'A', 'E', 'I', 'O', 'U',
        }
        lower2word = {}    
        for word in wordlist:
            if word.lower() in lower2word:
                continue
            lower2word[word.lower()] = word
            key = "".join([ch if ch not in vowels else "*" for ch in word]).lower()
            if key in lower2word:
                continue
            lower2word[key] = word

        answer = []
        for query in queries:
            val = ""
            if query in words:
                val = query
            elif query.lower() in lower2word:
                val = lower2word[query.lower()]
            else:
                key = "".join([ch if ch not in vowels else "*" for ch in query]).lower()
                if key in lower2word:
                    val = lower2word[key]
                
            answer.append(val)

        return answer
