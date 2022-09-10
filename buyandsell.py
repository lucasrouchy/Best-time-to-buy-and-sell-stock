
import math
class Solution:
    def maxProfit(k: int, prices: 'list[int]') -> int:
        temp = 0
        if not prices: return 0
        
        n = len(prices)
        #if k is greater than or eqaul to half the len of the prices list
        if k >= n//2:
            # returns the sum of x- y if x > y in the tuple created by the zip function where prices[1:] = all the prices execept the first one and prices[:-1] is all the prices except for the last one
            return sum( x - y for x, y in zip(prices[1:], prices[:-1]) if x > y)
        #profit variable = starter index * len of prices. this is done to make profit a list variable that will represent the local maxium
        profit = [0]* n
        #for each possible trade
        for j in range(k):
            #pre profit variable made to be able to compare to the profit in the for loop
            pre = 0
            #for each share price starting at index 1
            for i in range(1,n):
                #profits variable finding the difference btween the 2nd indexed price and the first.
                profits = prices[i] - prices[i -1]
                #pre proffits varaible is equal to the variable with the most current profit
                pre = max(pre + profits, profit[i])
                #make sure the profit list variable takes the max of all the possible profits
                profit[i] = max(profit[i-1], pre)
        #return profit[-1] because that is an easy way to access the ints at the end of the list variable
        return profit[-1]
            
        
        
        
    n = maxProfit(2 ,[2,4,1])
    m = maxProfit(2,[3,2,6,5,0,3])
    print(n)
    print(m)