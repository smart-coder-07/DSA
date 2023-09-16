#BRUTE FORCE SOLUTION OF MAXIMUM PRODUCT OF SUBARRAY.
                #Approach
#store first element in a variable max sub
#start loop 1 to n
#take one variable for current sum = 1
#start loop i to n store current sum *= a[i]
#compare current sum and maximum sum
#TIME COMPLEXITY O(N^2)
#SPACE COMPLEXITY O(1)
class Solution:
    def maxProduct(self, nums):
        ms= nums[0]
        for i in range(len(nums)):
            cs=1
            for j in range(i,len(nums)):
                cs=cs*nums[j]
                ms = max(cs,ms)
        return ms
ob = Solution()
nums = [1,2,0,4,5]
print(ob.maxProduct(nums))

#OPTIMAL SOLUTION
#OBSERVETION APPROACH
#take one variable max which initialize - infinity
#First we check 0 where have left side 0 area is called prefix right side area calle surfix.
#prefix start index 0 and surfix n-1
#store prefix area product in prefix variable and surfix also.
#if we found any 0 so make prifix 1 or surfix 1
#compare the product in max product variable
#Time Complexity = O(N)
#Space Complexity = O(1)
import math
class Optimal:
    def maxProduct(self, nums):
        mx = -math.inf
        prefix = 1
        surfix = 1
        n=len(nums)
        for i in range(n):
            if prefix == 0 : prefix = 1
            if surfix == 0 : surfix = 1
            prefix*=nums[i]
            surfix*=nums[n-i-1]
            mx = max(mx,max(prefix,surfix))
        return mx
ab = Optimal()
num1 = [1,2,0,4,5]
print(ab.maxProduct(num1))