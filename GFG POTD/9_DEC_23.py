class Solution:
    def countSubarrays(self, a,n,L,R): 
        # Complete the function
        initial = 0
        current = 0
        result = 0
        
        for i in range(n):
            if a[i]>=L and a[i]<=R:
                current = i - initial + 1
            elif a[i]>=R:
                initial = i + 1
                current = 0
            result = result + current
        return result
