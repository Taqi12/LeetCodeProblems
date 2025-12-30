class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # if n == 0:
        #     return nums1

        # for i in range(m, m + n):
        #     nums1[i] = nums2[i - m]

        # nums1.sort()

        left = m - 1
        right = n - 1
        k = m + n - 1

        while (left >= 0 and right >= 0):

            if nums1[left] > nums2[right]:
                nums1[k] = nums1[left]
                left -= 1
                k -= 1
            else:
                nums1[k] = nums2[right]
                right -= 1
                k -= 1

        while (right >= 0):
            nums1[k] = nums2[right]
            right -= 1
            k -= 1
 
