from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if (prices[j] - prices[i] > profit):
                    profit = prices[j] - prices[i]
        
        return profit


if __name__ == '__main__':
    for i in range(int(input())):
        prices = [int(x) for x in input().split()]

        obj = Solution()
        print(obj.maxProfit(prices))
