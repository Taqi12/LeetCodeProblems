class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        total_sum = 0
        negative_count = 0
        min_abs = float("inf")

        for row in matrix:

            for val in row:
                if val < 0:
                    negative_count += 1

                total_sum += abs(val)
                min_abs = min(min_abs, abs(val))

        if negative_count % 2 == 1:
            total_sum -= 2 * min_abs

        return total_sum 
        