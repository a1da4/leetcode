class Solution:
    def isNumber(self, s: str) -> bool:
        if 'inf' in s.lower() or 'nan' in s.lower():
            return False
        try:
            n = float(s)
            return True
        except:
            return False
