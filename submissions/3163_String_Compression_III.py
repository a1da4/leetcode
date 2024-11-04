class Solution:
    def compressedString(self, word: str) -> str:
        answer = ""
        prev = ""
        count = 0
        for ch in word:
            if prev == ch:
                count += 1
                if count > 9:
                    answer += f"9{prev}"
                    count -= 9
            else:
                if count > 0:
                    answer += f"{count}{prev}"
                    count = 0
                prev = ch
                count = 1
        
        if prev and count > 0:
            answer += f"{count}{prev}"

        return answer

