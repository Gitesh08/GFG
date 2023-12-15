class Solution:
	def nthPoint(self,n):
		# Code here
        mod = (10**9)+7
        x = 2
        y = 1
        for i in range(2,n+1):
            ans = (x+y)%mod
            y = x
            x = ans
        return y
