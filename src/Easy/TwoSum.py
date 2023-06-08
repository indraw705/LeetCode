# Link : https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i == j:
                    continue
                else:
                    if nums[i] + nums[j] == target:
                        return [i, j]


obj = Solution()
print(obj.twoSum([1, 2, 3, 4], 7))
print(obj.twoSum([1, 2, 3, 4], 5))
print(obj.twoSum([9, 2, 8, 4], 10))
print(obj.twoSum([5, 1, 7, 8], 8))
