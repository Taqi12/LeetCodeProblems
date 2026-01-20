class Solution:
    def minBitwiseArray(self, nums):

        ans = [-1] * len(nums)

        for idx, num in enumerate(nums):
            if num %2 == 0: continue    # <-- evens case  

            if  num %4 == 1:            # <-- 4 mod 1 case
                ans[idx] = num - 1 

            else:                       # <-- 4 mod 3 case
                tmp, i = num, 0
                for i in range(1,32):
                    tmp //= 2
                    if not tmp%2: break
                ans[idx] = num - (1<<(i-1))

        return ans