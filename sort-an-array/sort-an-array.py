class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        left, right = self.sortArray(nums[:len(nums)//2]),self.sortArray(nums[len(nums)//2:])
        return self.Merge(left, right)
    
    def Merge(self, left, right): 
        l, r = 0, 0 
        result = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        if l == len(left):
            result += right[r:]
        else:
            result += left[l:]
        return result 