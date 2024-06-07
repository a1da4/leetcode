class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        answer = []
        dictionary.sort()
        for word in sentence.split():
            replace = None
            for root in dictionary:
                if len(root) <= len(word) and root == word[:len(root)]:
                    replace = root
                    break
            if replace is None:
                replace = word
            answer.append(replace)

        return " ".join(answer)

