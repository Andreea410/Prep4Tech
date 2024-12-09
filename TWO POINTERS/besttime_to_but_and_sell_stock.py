# 121. Best Time to Buy and Sell Stock
# Solved
# Easy
# Topics
# Companies
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy , sell = 0 , 1
        maximum_profit = 0
        while sell < len(prices):
            current_profit = prices[sell] - prices[buy]
            if current_profit > maximum_profit:
                maximum_profit = current_profit
            else:
                if prices[sell] < prices[buy]:
                    buy = sell
            sell+=1
        return maximum_profit

----------------------OR ---------------------------------
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maximum_profit = 0
        left = 0
        right = 1
        while right < len(prices):
            current_profit = prices[right] - prices[left]
            if current_profit < 0:
                left += 1
                right -= 1
            maximum_profit = max(maximum_profit , current_profit)
            right +=1

        return maximum_profit

