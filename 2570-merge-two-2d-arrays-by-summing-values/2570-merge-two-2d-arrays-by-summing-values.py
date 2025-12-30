class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
                
        dict = {}
        result = []

        for i in nums1:
            if i[0] not in dict:
                dict[i[0]] = i[1]
            else:
                dict[i[0]] += i[1]

        for i in nums2:
            if i[0] not in dict:
                dict[i[0]] = i[1]
            else:
                dict[i[0]] += i[1]

        # Sort by keys before appending to the result list
        for key in sorted(dict.keys()):
            result.append([key, dict[key]])

        return result