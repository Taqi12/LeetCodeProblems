class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        total = n * m
        pref, suf = [0]*total, [0]*total
        res = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                idx = i*m+j
                pref[idx] = (pref[idx-1]*grid[i][j])%MOD if idx>0 else grid[i][j]%MOD
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                idx = i*m+j
                suf[idx] = (suf[idx+1]*grid[i][j])%MOD if idx<total-1 else grid[i][j]%MOD
        for i in range(n):
            for j in range(m):
                idx = i*m+j
                l = pref[idx-1] if idx>0 else 1
                r = suf[idx+1] if idx<total-1 else 1
                res[i][j] = (l*r)%MOD
        return res