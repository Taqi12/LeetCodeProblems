class Solution:
    def calculatePrefixSum(self, grid: List[List[str]], targetChar: str) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        
        prefixSum = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                prefixSum[row][col] = 1 if grid[row][col] == targetChar else 0
                if row > 0: prefixSum[row][col] += prefixSum[row - 1][col]
                if col > 0: prefixSum[row][col] += prefixSum[row][col - 1]
                if row > 0 and col > 0: prefixSum[row][col] -= prefixSum[row - 1][col - 1]
        
        return prefixSum
    
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        xCountPrefixSum = self.calculatePrefixSum(grid, 'X')
        yCountPrefixSum = self.calculatePrefixSum(grid, 'Y')
        
        matchingSubmatricesCount = 0
        for row in range(rows):
            for col in range(cols):
                if xCountPrefixSum[row][col] == yCountPrefixSum[row][col] and xCountPrefixSum[row][col] > 0:
                    matchingSubmatricesCount += 1
        
        return matchingSubmatricesCount