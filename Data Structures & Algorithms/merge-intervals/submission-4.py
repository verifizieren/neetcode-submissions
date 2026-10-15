class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        sortedIntervals = sorted(map(tuple, intervals), key=lambda x:x[0])
        
        prevStart = sortedIntervals[0][0]
        prevEnd = sortedIntervals[0][1]
        res = []

        for start, end in sortedIntervals[1:]:
            if start <= prevEnd:
                prevEnd = max(prevEnd, end)
            else:
                res.append([prevStart, prevEnd])
                prevStart = start
                prevEnd = end
        res.append([prevStart, prevEnd])

        return res