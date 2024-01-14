class Solution:
    def find3Numbers(self,A, n, X):
        A.sort()
        
        for i in range(n-2):
            l = i+1
            r = n-1
            
            while l < r:
                
                total = A[i] + A[l] + A[r]
                
                if total == X:
                    return True
                
                elif total > X:
                    r -=1
                else:
                    l +=1
                    
        return False
