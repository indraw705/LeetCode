class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        cols = []

        for i in range(len(grid)):
            col_val = []
            for j in range(len(grid)):
                col_val.append(grid[j][i])
            cols.append(col_val)
        for i in grid:
            if i in cols:
                count = count + cols.count(i)
        return count

obj1=Solution()
# print(obj1.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
# print(obj1.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(obj1.equalPairs([[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]))

 # [3,1,2,2]
 # [1,4,4,4]
 # [2,4,2,2]
 # [2,5,2,2]