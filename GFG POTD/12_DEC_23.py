class Solution:

    def maxGold(self, n, m, M):
        knap={}
        
        def func(i,j):

            if i==n or j==m or i<0 or j<0:
                return 0
            
            if (i,j) in knap:
                return knap[(i,j)]

            knap[(i,j)]=M[i][j] + max(func(i+1,j+1),func(i,j+1),func(i-1,j+1))

            return knap[(i,j)]

        ans=0

        for i in range(n):

            ans=max(ans, func(i,0))

        return ans
