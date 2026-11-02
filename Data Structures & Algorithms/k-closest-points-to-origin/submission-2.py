class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [tuple(x) for x in points]
        minDist = [-(x[0]**2 + x[1]**2) for x in points]

        act = list(zip(minDist, minHeap))
        heapq.heapify(act)

        while len(act) > k:
            heapq.heappop(act)
        
        return [list(item[1]) for item in act]