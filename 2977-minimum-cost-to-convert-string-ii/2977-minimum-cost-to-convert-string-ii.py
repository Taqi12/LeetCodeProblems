class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        idx_map = {}
        count = 0
        for o in original:
            if o not in idx_map:
                idx_map[o] = count
                count += 1
        for c in changed:
            if c not in idx_map:
                idx_map[c] = count
                count += 1
        
        INF = float('inf')
        dist = [[INF] * count for _ in range(count)]
        for i in range(count):
            dist[i][i] = 0

        for o, c, val in zip(original, changed, cost):
            u, v = idx_map[o], idx_map[c]
            dist[u][v] = min(dist[u][v], val)

        for k in range(count):
            for i in range(count):
                if dist[i][k] == INF:
                    continue
                for j in range(count):
                    if dist[k][j] != INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        possible = sorted(list(set(len(o) for o in original)))
        n = len(source)

        dp = [INF] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            if source[i] == target[i]:
                dp[i] = dp[i + 1]
            for p in possible:
                if i + p > n:
                    break
                sub_s = source[i : i + p]
                sub_t = target[i : i + p]
                if sub_s in idx_map and sub_t in idx_map:
                    u, v = idx_map[sub_s], idx_map[sub_t]
                    if dist[u][v] != INF:
                        if dp[i + p] != INF:
                            dp[i] = min(dp[i], dist[u][v] + dp[i + p])

        return dp[0] if dp[0] != INF else -1
