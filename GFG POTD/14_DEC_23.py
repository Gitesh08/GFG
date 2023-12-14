class Solution:
    def countWays(self,n,k):
        #code here.
        fi = k
        se = k**2
        if n == 1:
            return k
        sum1 = k**2
        for i in range(n-2):
            sum1 = ((fi + se)*(k-1)) % ((10**9)+7)
            fi = se
            se = sum1
        return sum1
