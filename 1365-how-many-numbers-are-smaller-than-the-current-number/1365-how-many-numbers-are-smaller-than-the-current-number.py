class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = [0]*1000
        answer = []
        
        for i in nums:
            result[i] = 0
            for j in range(len(nums)):
                if i>nums[j]:
                    result[i] = result[i]+1
                else:
                    continue
            
            answer.append(result[i])
        return answer