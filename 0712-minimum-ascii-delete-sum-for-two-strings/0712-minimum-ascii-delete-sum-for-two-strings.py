class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        dp = [0] * (n + 1)

        for i in range(m):
            prev = 0
            for j in range(n):
                temp = dp[j + 1]
                if s1[i] == s2[j]:
                    dp[j + 1] = prev + ord(s1[i])
                else:
                    dp[j + 1] = max(dp[j + 1], dp[j])
                prev = temp

        total_sum = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        return total_sum - 2 * dp[n]
