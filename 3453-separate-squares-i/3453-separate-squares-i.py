class Solution:
    def separateSquares(self, squares):
        # Total area
        total_area = 0
        min_y = float('inf')
        max_y = 0

        for x, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)

        target = total_area / 2.0

        # Function to compute area below Y
        def area_below(Y):
            area = 0.0
            for x, y, l in squares:
                if Y <= y:
                    continue
                elif Y >= y + l:
                    area += l * l
                else:
                    area += l * (Y - y)
            return area

        # Binary search
        left, right = min_y, max_y
        for _ in range(60):  # enough for 1e-5 precision
            mid = (left + right) / 2
            if area_below(mid) < target:
                left = mid
            else:
                right = mid

        return left
