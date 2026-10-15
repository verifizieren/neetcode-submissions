class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sortedIntervals = sorted(map(tuple, intervals), key=lambda x:x[0])

        count = 0
        prevEnd = sortedIntervals[0][1]

        for start, end in sortedIntervals[1:]:
            if start < prevEnd:
                count += 1
                prevEnd = min(end, prevEnd)
            else:
                prevEnd = end

        return count