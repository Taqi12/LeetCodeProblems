class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:

        def max_consecutive_gap(bars):
            bars.sort()
            max_streak = 1
            curr = 1

            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    curr += 1
                    max_streak = max(max_streak, curr)
                else:
                    curr = 1

            return max_streak + 1  # +1 for gap size

        max_height = max_consecutive_gap(hBars)
        max_width = max_consecutive_gap(vBars)

        side = min(max_height, max_width)
        return side * side
