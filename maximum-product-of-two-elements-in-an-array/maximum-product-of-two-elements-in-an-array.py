import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        nums.sort()
        return ((nums[-1]-1)*(nums[-2]-1))