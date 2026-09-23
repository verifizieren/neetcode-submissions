class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s1.sort()
        l = 0
        
        for r in range(len(s1) -1, len(s2)):
            curstr = list(s2)[l:r+1]
            curstr.sort()
            if curstr == s1:
                return True

            l+=1
        return False
    
