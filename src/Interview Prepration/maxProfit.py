class Solution:
    def maxProfit(self, prices) -> int:
        left = 0
        right = 1
        max_profit = 0
        while right != len(prices):
            if left == len(prices):
                break
            else:
                if prices[left] < prices[right]:
                    current_profit = prices[right] - prices[left]
                    if max_profit < current_profit:
                        max_profit = current_profit
                right += 1
            if right == len(prices):
                left += 1
                right = left + 1
        return max_profit

obj1 = Solution()
print(obj1.maxProfit([7, 1, 5, 3, 10, 4]))
# print(obj1.maxProfit([3, 4, 8]))
