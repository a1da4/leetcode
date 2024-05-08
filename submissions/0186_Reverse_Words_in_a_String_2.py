class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        words = ''.join(s).split()
        for sId, ch in enumerate(' '.join(words[::-1])):
            s[sId] = ch
