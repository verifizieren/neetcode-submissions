class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        best = 0
        maxf = 0

        for r, val in enumerate(s):
            count[val] += 1
            maxf = max(maxf, count[val])

            while (r - l + 1) - maxf > k:
                count[s[l]] -=1
                l +=1
            
            best = max(best, r - l + 1)
        return best


                