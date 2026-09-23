class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         freq = Counter(nums)
         topk = heapq.nlargest(k, freq.items(), key=lambda x: x[1])

         return [num for num, _ in topk]

        