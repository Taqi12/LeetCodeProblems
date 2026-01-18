class Solution:
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])

        # Prefix sums
        rowSum = [[0] * (n + 1) for _ in range(m)]
        colSum = [[0] * n for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                rowSum[i][j + 1] = rowSum[i][j] + grid[i][j]
                colSum[i + 1][j] = colSum[i][j] + grid[i][j]

        # Try larger squares first
        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):

                    # Target sum = first row
                    target = rowSum[i][j + k] - rowSum[i][j]
                    valid = True

                    # Check all rows
                    for r in range(i, i + k):
                        if rowSum[r][j + k] - rowSum[r][j] != target:
                            valid = False
                            break

                    if not valid:
                        continue

                    # Check all columns
                    for c in range(j, j + k):
                        if colSum[i + k][c] - colSum[i][c] != target:
                            valid = False
                            break

                    if not valid:
                        continue

                    # Check diagonals
                    diag1 = diag2 = 0
                    for d in range(k):
                        diag1 += grid[i + d][j + d]
                        diag2 += grid[i + d][j + k - 1 - d]

                    if diag1 == target and diag2 == target:
                        return k

        return 1
