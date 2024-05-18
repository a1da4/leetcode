class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def is_shifted(word_1: str, word_2: str) -> bool:
            if len(word_1) != len(word_2):
                return False
            if len(word_1) == 1:
                return True
            shift = (ord(word_1[0]) - ord(word_2[0])) % 26
            for ch_1, ch_2 in zip(word_1[1:], word_2[1:]):
                if (ord(ch_1) - ord(ch_2)) % 26 != shift:
                    return False
            return True

        answer = []
        while strings:
            word_1 = strings.pop(0)
            currGroup = [word_1]
            _strings = []
            for word_2 in strings:
                if is_shifted(word_1, word_2):
                    currGroup.append(word_2)
                else:
                    _strings.append(word_2)
            answer.append(currGroup)
            strings = _strings
        return answer

