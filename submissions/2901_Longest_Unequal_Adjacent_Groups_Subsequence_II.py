class Solution:
    def getWordsInLongestSubsequence(
        self, 
        words: List[str], 
        groups: List[int],
    ) -> List[str]:

        def verified(word_i, word_j) -> bool:
            if len(word_i) != len(word_j):
                return False
            diff = 0
            for ch_i, ch_j in zip(
                word_i, word_j
            ):
                if ch_i != ch_j:
                    diff += 1
            return diff == 1

        answer = []
        N = len(words)
        dp = [1] * N
        prev = [-1] * N
        maxId = 0

        for i in range(1, N):
            for j in range(i):
                if (
                    verified(words[i], words[j])
                    and dp[j] + 1 > dp[i]
                    and groups[i] != groups[j]
                ):
                    dp[i] = dp[j] + 1
                    prev[i] = j
                
            if dp[i] > dp[maxId]:
                maxId = i
        
        i = maxId
        while i >= 0:
            answer.append(words[i])
            i = prev[i]

        return answer[::-1]
class Solution:
    def getWordsInLongestSubsequence(
        self, 
        words: List[str], 
        groups: List[int],
    ) -> List[str]:

        def verified(word_i, word_j) -> bool:
            if len(word_i) != len(word_j):
                return False
            diff = 0
            for ch_i, ch_j in zip(
                word_i, word_j
            ):
                if ch_i != ch_j:
                    diff += 1
            return diff == 1

        answer = []
        N = len(words)
        dp = [1] * N
        prev = [-1] * N
        maxId = 0

        for i in range(1, N):
            for j in range(i):
                if (
                    verified(words[i], words[j])
                    and dp[j] + 1 > dp[i]
                    and groups[i] != groups[j]
                ):
                    dp[i] = dp[j] + 1
                    prev[i] = j
                
            if dp[i] > dp[maxId]:
                maxId = i
        
        i = maxId
        while i >= 0:
            answer.append(words[i])
            i = prev[i]

        return answer[::-1]
class Solution:
    def getWordsInLongestSubsequence(
        self, 
        words: List[str], 
        groups: List[int],
    ) -> List[str]:

        def verified(word_i, word_j) -> bool:
            if len(word_i) != len(word_j):
                return False
            diff = 0
            for ch_i, ch_j in zip(
                word_i, word_j
            ):
                if ch_i != ch_j:
                    diff += 1
            return diff == 1

        answer = []
        N = len(words)
        dp = [1] * N
        prev = [-1] * N
        maxId = 0

        for i in range(1, N):
            for j in range(i):
                if (
                    verified(words[i], words[j])
                    and dp[j] + 1 > dp[i]
                    and groups[i] != groups[j]
                ):
                    dp[i] = dp[j] + 1
                    prev[i] = j
                
            if dp[i] > dp[maxId]:
                maxId = i
        
        i = maxId
        while i >= 0:
            answer.append(words[i])
            i = prev[i]

        return answer[::-1]
class Solution:
    def getWordsInLongestSubsequence(
        self, 
        words: List[str], 
        groups: List[int],
    ) -> List[str]:

        def verified(word_i, word_j) -> bool:
            if len(word_i) != len(word_j):
                return False
            diff = 0
            for ch_i, ch_j in zip(
                word_i, word_j
            ):
                if ch_i != ch_j:
                    diff += 1
            return diff == 1

        answer = []
        N = len(words)
        dp = [1] * N
        prev = [-1] * N
        maxId = 0

        for i in range(1, N):
            for j in range(i):
                if (
                    verified(words[i], words[j])
                    and dp[j] + 1 > dp[i]
                    and groups[i] != groups[j]
                ):
                    dp[i] = dp[j] + 1
                    prev[i] = j
                
            if dp[i] > dp[maxId]:
                maxId = i
        
        i = maxId
        while i >= 0:
            answer.append(words[i])
            i = prev[i]

        return answer[::-1]
class Solution:
    def getWordsInLongestSubsequence(
        self, 
        words: List[str], 
        groups: List[int],
    ) -> List[str]:

        def verified(word_i, word_j) -> bool:
            if len(word_i) != len(word_j):
                return False
            diff = 0
            for ch_i, ch_j in zip(
                word_i, word_j
            ):
                if ch_i != ch_j:
                    diff += 1
            return diff == 1

        answer = []
        N = len(words)
        dp = [1] * N
        prev = [-1] * N
        maxId = 0

        for i in range(1, N):
            for j in range(i):
                if (
                    verified(words[i], words[j])
                    and dp[j] + 1 > dp[i]
                    and groups[i] != groups[j]
                ):
                    dp[i] = dp[j] + 1
                    prev[i] = j
                
            if dp[i] > dp[maxId]:
                maxId = i
        
        i = maxId
        while i >= 0:
            answer.append(words[i])
            i = prev[i]

        return answer[::-1]
class Solution:
    def getWordsInLongestSubsequence(
        self, 
        words: List[str], 
        groups: List[int],
    ) -> List[str]:

        def verified(word_i, word_j) -> bool:
            if len(word_i) != len(word_j):
                return False
            diff = 0
            for ch_i, ch_j in zip(
                word_i, word_j
            ):
                if ch_i != ch_j:
                    diff += 1
            return diff == 1

        answer = []
        N = len(words)
        dp = [1] * N
        prev = [-1] * N
        maxId = 0

        for i in range(1, N):
            for j in range(i):
                if (
                    verified(words[i], words[j])
                    and dp[j] + 1 > dp[i]
                    and groups[i] != groups[j]
                ):
                    dp[i] = dp[j] + 1
                    prev[i] = j
                
            if dp[i] > dp[maxId]:
                maxId = i
        
        i = maxId
        while i >= 0:
            answer.append(words[i])
            i = prev[i]

        return answer[::-1]
class Solution:
    def getWordsInLongestSubsequence(
        self, 
        words: List[str], 
        groups: List[int],
    ) -> List[str]:

        def verified(word_i, word_j) -> bool:
            if len(word_i) != len(word_j):
                return False
            diff = 0
            for ch_i, ch_j in zip(
                word_i, word_j
            ):
                if ch_i != ch_j:
                    diff += 1
            return diff == 1

        answer = []
        N = len(words)
        dp = [1] * N
        prev = [-1] * N
        maxId = 0

        for i in range(1, N):
            for j in range(i):
                if (
                    verified(words[i], words[j])
                    and dp[j] + 1 > dp[i]
                    and groups[i] != groups[j]
                ):
                    dp[i] = dp[j] + 1
                    prev[i] = j
                
            if dp[i] > dp[maxId]:
                maxId = i
        
        i = maxId
        while i >= 0:
            answer.append(words[i])
            i = prev[i]

        return answer[::-1]
class Solution:
    def getWordsInLongestSubsequence(
        self, 
        words: List[str], 
        groups: List[int],
    ) -> List[str]:

        def verified(word_i, word_j) -> bool:
            if len(word_i) != len(word_j):
                return False
            diff = 0
            for ch_i, ch_j in zip(
                word_i, word_j
            ):
                if ch_i != ch_j:
                    diff += 1
            return diff == 1

        answer = []
        N = len(words)
        dp = [1] * N
        prev = [-1] * N
        maxId = 0

        for i in range(1, N):
            for j in range(i):
                if (
                    verified(words[i], words[j])
                    and dp[j] + 1 > dp[i]
                    and groups[i] != groups[j]
                ):
                    dp[i] = dp[j] + 1
                    prev[i] = j
                
            if dp[i] > dp[maxId]:
                maxId = i
        
        i = maxId
        while i >= 0:
            answer.append(words[i])
            i = prev[i]

        return answer[::-1]

