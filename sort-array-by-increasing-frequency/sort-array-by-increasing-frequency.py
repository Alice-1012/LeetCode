class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
 
        pq = []
        for key, value in counter.items():
            heapq.heappush(pq, (value, -key))
        
        results = []
        for i in range(len(pq)):
            count, value = heapq.heappop(pq)
            for j in range(count):
                results.append(-value)
        
        return results  