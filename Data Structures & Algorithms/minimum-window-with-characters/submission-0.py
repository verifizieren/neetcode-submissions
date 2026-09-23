class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)

        l = start = end = 0

        for r, ch in enumerate(s, 1):   # r is 1-based
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            if missing == 0:
                # shrink from left
                while need[s[l]] < 0:
                    need[s[l]] += 1
                    l += 1

                # update best
                if end == 0 or r - l < end - start:
                    start, end = l, r

                # move left forward for next window
                need[s[l]] += 1
                missing += 1
                l += 1

        return s[start:end]

