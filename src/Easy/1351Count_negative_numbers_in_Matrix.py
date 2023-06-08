# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

class Solution:
    def countNegatives(self, grid):
        count = 0
        for row in grid:
            for cell in row:
                if cell < 0:
                    count = count + 1
        return count


obj = Solution()
print(obj.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
print(obj.countNegatives([[3,2],[1,0]]))
