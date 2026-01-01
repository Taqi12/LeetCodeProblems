class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        n = len(nums)
        dict = {}
        duplicate = -1
        missing = -1

        # find duplicate
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
            if dict[num] == 2:
                duplicate = num
        
        # find missing
        for i in range(1, n + 1): 
            if i not in dict:
                missing = i
                break # once found missing number, then no need to continue

        return [duplicate, missing]
        