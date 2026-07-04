class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0

        for i in range(len(prices) - 1):
            maxProfit = max(maxProfit, prices[right]-prices[left])
            if prices[left] >= prices[right]:
                left = right
                right += 1
            else:
                right += 1
            
        return maxProfit

    