# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, heights: List[int]) -> int:

        tallest_left = []
        tallest_seen = 0
        for c in heights:
            tallest_left.append(tallest_seen)
            if c > tallest_seen:
                tallest_seen = c

        tallest_right = []
        tallest_seen  = 0
        for c in heights[::-1]:
            tallest_right.append(tallest_seen)
            if c > tallest_seen:
                tallest_seen = c
        tallest_right = tallest_right[::-1]

        allowed_water_height = [min(left,right) for left,right, in zip(tallest_left, tallest_right)]
        actual_water_level = [max(0, water_level-terrain_level) for water_level, terrain_level in zip(allowed_water_height, heights)]

        return sum(actual_water_level)
