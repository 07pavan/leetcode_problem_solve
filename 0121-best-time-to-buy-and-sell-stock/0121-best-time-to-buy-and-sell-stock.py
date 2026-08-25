class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p=prices[0]
        max_p=0
        for pri in prices[1:]:
            profit=pri-min_p
            max_p=max(max_p,profit)
            min_p=min(min_p,pri)
        return max_p
