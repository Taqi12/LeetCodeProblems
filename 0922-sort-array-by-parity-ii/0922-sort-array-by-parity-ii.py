class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        l = 0
        r = 1

        while (l < len(nums) and r < len(nums)):

            if nums[l] % 2 == 0 and nums[r] % 2 != 0:
                l += 2
                r += 2
                
            elif nums[l] % 2 == 0:
                l += 2

            elif nums[r] % 2 != 0:
                r += 2
            
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 2
                r += 2

        return nums
                