# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def fn(n,x):
            if n<x:
                return n*(2*x-n+1)//2

            return x*(1+x)//2+n-x

        low,high=0,maxSum
        while low<high:
            mid=low+high+1>>1
            sm=fn(index,mid-1)+fn(n-index,mid)
            if sm<=maxSum:
                low=mid

            else:
                high=mid-1

        return low

obj = Solution()
print(obj.maxValue(4,2,6))    #2
print(obj.maxValue(6,1,10))    #3