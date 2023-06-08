# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
class Solution:
    def canMakeArithmeticProgression(self, arr) :
        if len(arr) == 2:
            return True
        else:
            sorted_arr = sorted(arr)
            print(sorted_arr)
            difference = sorted_arr[1] - sorted_arr[0]
            for i in range(len(sorted_arr) - 1):
                if sorted_arr[i + 1] - sorted_arr[i] != difference:
                    return False
                else:
                    if i == len(sorted_arr) - 2:
                        return True
                    continue


obj = Solution()
print(obj.canMakeArithmeticProgression([3,5,1]))
print(obj.canMakeArithmeticProgression([2,3,4]))
print(obj.canMakeArithmeticProgression([5,7,8]))
print(obj.canMakeArithmeticProgression([1,6,11]))