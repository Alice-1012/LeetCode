class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        temp_dict = {}
        result = []
        for i in range(len(temp)):
            if (temp[i] not in temp_dict):
                temp_dict[temp[i]] = i
        for i in nums:
            result.append(temp_dict[i])
        return result