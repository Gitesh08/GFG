class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        #Your code here
        if m==n:
            return -1
        ans = m^n
        count = 1
        while not ans&1 :
            ans>>=1
            count+=1
        return count
