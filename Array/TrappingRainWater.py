                          #Approach
#1.First We Create Two Helping Arrays.
#2.First Array Store The All Left Most Boundaries.
#3.Second Array Store The All Right Most Boundaries.
#4.After That We Start single loop 0 to n and in this loop check
#which boundary is small and small boundary we store in any varible
#5.After That We substrack the min boundary and a[i] and add the variable
#in this which store the result of this and return the variable

                   #Time Complexity - O(n)
                   #Space Complexity - O(n)
#This solution is the optimal solution of this question and very easy to understand

class Solution:
    def trappingWater(self, a,n):
        l=[a[0]]
        for i in range(1,n):
            l.append(max(l[i-1],a[i]))
        r=[a[n-1]]
        k=0
        for i in range(n-2,-1,-1):
            r.append(max(r[k],a[i]))
            k+=1
        t=0
        r.reverse()
        for i in range(n):
            m=min(l[i],r[i])
            t=(m-a[i])+t
        return t

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()


