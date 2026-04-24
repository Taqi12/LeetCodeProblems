class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        
        net_change = 0
        underscores = 0

        for char in moves:
            if char == 'L':
                net_change -= 1
            elif char == 'R':
                net_change += 1
            else:
                underscores += 1


        return abs(net_change) + underscores

             