from math import gcd

class Solution:
    def maxPoints(self, points):
        n = len(points)
        slopes = [[[None] for i in range(n)] for i in range(n)]

        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if i == j:
                    slopes[i][j] = 'same'
                else:
                    deltaX = p2[0] - p1[0]
                    deltaY = p2[1] - p1[1]
                    if deltaX < 0:
                        deltaX = abs(deltaX)
                        deltaY = -deltaY

                    if deltaX == 0 and deltaY == 0:
                        slopes[i][j] = 'same'
                    elif deltaX == 0:
                        slopes[i][j] = 'inf'
                        slopes[j][i] = 'inf'
                    else:
                        gee_see_dee = gcd(deltaX, deltaY)
                        deltaX/=gee_see_dee
                        deltaY/=gee_see_dee
                        slopes[i][j] = str(deltaX)+'/'+str(deltaY)
                        slopes[j][i] = slopes[i][j]

        max_num_in_line = 0
        for i in range(n): # count max number of points lying on line that passes through points[i]
            all_slope_counts = {}
            for slope in slopes[i]:
                if slope != 'same':
                    if slope in all_slope_counts:
                        all_slope_counts[slope] += 1
                    else:
                        all_slope_counts[slope] = 1


            max_candidate = max(list(all_slope_counts.values())+[0]) + slopes[i].count('same')
            max_num_in_line = max(max_num_in_line, max_candidate)

        breakpoint()
        return max_num_in_line
