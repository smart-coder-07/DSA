#Brute Force Method
#time complexity --> O(n^3)
#Space complexity --> O(n)
import math
class Solution:
    def maxSubArraySum(self,l,N):
        c=-math.inf
        s=0
        for i in range(len(l)):
            l2=[]
            for j in range(i,len(l)):
                l2.append(l[j])
                s=sum(l2)
                if c<s:
                    c=s
        return c
import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()