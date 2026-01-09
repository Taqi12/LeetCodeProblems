class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        
        # DP table initialized with very small values
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                product = nums1[i - 1] * nums2[j - 1]
                
                # Either start new subsequence or extend previous one
                take = max(product, product + dp[i - 1][j - 1])
                
                # Choose the best option
                dp[i][j] = max(
                    take,
                    dp[i - 1][j],   # skip nums1 element
                    dp[i][j - 1]    # skip nums2 element
                )
        
        return dp[n][m]