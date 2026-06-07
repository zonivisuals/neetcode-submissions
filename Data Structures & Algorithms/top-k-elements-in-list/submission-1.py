import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1

        heap = []
        for key,v in dic.items():
            heapq.heappush(heap, (v,key))
            if (len(heap) > k):
                heapq.heappop(heap)

        res = [v for (k,v) in heap]
        return res