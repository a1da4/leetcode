class Solution:
    def getLongestSubsequence(
        self, 
        words: List[str], 
        groups: List[int],
    ) -> List[str]:
        answer = [words[0]]
        curr = groups[0]

        for word, group in zip(
            words[1:], groups[1:]
        ):
            if curr != group:
                answer.append(word)
                curr = group
            
        return answer

