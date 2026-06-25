class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        profit = 0
        for i in range(len(prices)-1):
            if prices[left] >= prices[right]:
                left = right
                right += 1
            else:
                if prices[right] - prices[left] > profit:
                    profit = prices[right] - prices[left]
                right += 1
        
        return profit
            
        
        