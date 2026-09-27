class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        maps = {}
        mapt = {}

        for ch in s:
            if ch not in maps:
                maps[ch] = 1
            else:
                maps[ch] += 1
        
        for ch in t:
            if ch not in mapt:
                mapt[ch] = 1
            else:
                mapt[ch] += 1
        
        return maps == mapt