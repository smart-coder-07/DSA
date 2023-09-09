#Maximum Difference Between Increasing Elements leetcode
#in this question we use two pointer approach
#Time Complexity --> O(n)
#Space Complexity --> O(1)
class Solution:
    def maximumDifference(self,a):
        x=0
        d=0
        for i in range(1,len(a)):
            if a[x]<a[i]:
                c=a[i]-a[x]
                d=max(c,d)
            else:
                x=i
        if d==0:
            return -1
        else:
            return d
a=[1,5,2,10]
ob=Solution()
print(ob.maximumDifference(a))
        