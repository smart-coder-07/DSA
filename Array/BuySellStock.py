#Best Time To Buy And Sell Stock For Profit Leetcode DSA.
#Two Pointer Approach Used This Question for solving it. 
#Time Complexity --> O(n)
#Space Complexity --> O(1)
import math
class Solution:
    def maxProfit(self, p):
        b=math.inf
        s=0
        profit=0
        for i in range(len(p)):
            if b<p[i]:
                s=p[i]
                c=s-b
                profit=max(profit,c)
            else:
                b=p[i]
        return profit
a=[7,1,5,3,6,4]
ob=Solution()
print(ob.maxProfit(a))