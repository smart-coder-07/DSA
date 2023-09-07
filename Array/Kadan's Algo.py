#Optimal Solution (Kadan's Algorithm)
#time complexity --> O(n)
#Space complexity --> O(1)
import math
class Solution:
    def kadans(self,l,n):
        cs=0
        ms=l[0]
        for i in range(n):
            cs+=l[i]
            ms=max(cs,ms)
            if cs<0:
                cs=0
        return ms
        
            
    
import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.kadans(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()