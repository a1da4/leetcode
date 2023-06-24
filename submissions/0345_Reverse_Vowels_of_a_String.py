class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        vowelIds = []
        for currId, currChar in enumerate(s):
            if currChar in set(["a", "i", "u", "e", "o", "A", "I", "U", "E", "O"]):
                vowels.append(currChar)
                vowelIds.append(currId)
        vowels = vowels[::-1]
        
        answer = ""
        if len(vowels) == 0:
            answer = s[:]
        else:
            vowelId = vowelIds.pop(0)
            for currId, currChar in enumerate(s):
                if currId == vowelId:
                    answer += vowels.pop(0)
                    if len(vowelIds) > 0:
                        vowelId = vowelIds.pop(0)
                else:
                    answer += currChar
        return answer
