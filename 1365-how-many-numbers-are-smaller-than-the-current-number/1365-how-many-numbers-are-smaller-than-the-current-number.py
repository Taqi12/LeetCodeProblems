class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        sorted_nums = sorted(nums)
        dict = {}

        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in dict:
                dict[sorted_nums[i]] = i

        result = []

        for i in nums:
            result.append(dict[i])

        return result

        