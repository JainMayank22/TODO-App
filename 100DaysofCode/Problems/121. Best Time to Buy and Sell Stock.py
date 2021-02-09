class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        max_profit = 0

        for i in range(1,len(prices)):
            profit = prices[i]-buy

            if profit>max_profit:
                max_profit = profit

            if buy>prices[i]:
                buy = prices[i]

        return max_profit
