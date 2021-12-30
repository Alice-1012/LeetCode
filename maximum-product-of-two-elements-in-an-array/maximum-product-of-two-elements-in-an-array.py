import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = nums[:2]
        heapq.heapify(heap)
        
        for i in range(2, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappushpop(heap, nums[i])
                
        return  (heap[0] - 1) * (heap[1] - 1)