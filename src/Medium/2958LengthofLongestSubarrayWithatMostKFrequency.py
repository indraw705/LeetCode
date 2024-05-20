# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/?envType=daily-question&envId=2024-03-28
class Solution:
    def maxSubarrayLength(self, nums):
        a = nums
        b = a
        k = 1
        d = {}
        left = 0
        max_len = 0
        for i in range(0, len(a)):
            if a[i] in d:
                d[a[i]] += 1
                if k >= d[a[i]]:
                    d[a[i]] = int(d[a[i]]) + 1
                else:
                    while(d[a[i]]>k):
                        d[a[left]] -= 1
                        left += 1
                    if(i-left> max_len):
                        max_len = i-left
            else:
                d[a[i]] = 1
                if k < d[a[i]]:
                    while (d[a[i]] > k):
                        d[a[left]] -= 1
                        left += 1
                    if (i - left > max_len):
                        max_len = i - left

        return len(b)

obj = Solution()
# print(obj.maxSubarrayLength([5,5,5,5,5,5,5]))
print(obj.maxSubarrayLength([1,4,4,3]))