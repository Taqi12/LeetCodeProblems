class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        result = []
        for num in nums:
            if num % 2 == 0:
                result.append(num)
        for num in nums:
            if num % 2 != 0:
                result.append(num)

        return result

        # Approach 2

        l = 0
        r = len(nums) - 1

        while (l < r):
            if nums[l] % 2 != 0 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            
            elif (nums[l] % 2 == 0):
                l += 1
            else:
                r -= 1

        return nums
            