
import math
class Solution:
    def maxProfit(k: int, prices: 'list[int]') -> int:
        temp = 0
        if not prices: return 0
        profit = 0
        n = len(prices)
        #if k is greater than or eqaul to half the len of the prices list
        if k >= n//2:
            # returns the sum of x- y if x > y in the tuple created by the zip function where prices[1:] = all the prices execept the first one and prices[:-1] is all the prices except for the last one
            return sum( x - y for x, y in zip(prices[1:], prices[:-1]) if x > y)

            
        
        
        
    maxProfit(2 ,[2,4,1])
    maxProfit(2,[3,2,6,5,0,3])