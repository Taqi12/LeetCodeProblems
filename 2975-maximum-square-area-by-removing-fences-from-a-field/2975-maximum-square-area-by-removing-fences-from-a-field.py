class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        MOD = 10**9 + 7

        # Add boundary fences
        h = sorted([1] + hFences + [m])
        v = sorted([1] + vFences + [n])

        # Compute all possible horizontal gaps
        h_gaps = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_gaps.add(h[j] - h[i])

        # Compute all possible vertical gaps
        v_gaps = set()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                v_gaps.add(v[j] - v[i])

        # Find largest common gap
        common = h_gaps & v_gaps
        if not common:
            return -1

        side = max(common)
        return (side * side) % MOD
