class Solution:    
    def countX(self,L,R,X):
        #code here
        self.L = L
        self.R = R
        hod = []
        cnt =0
        
        for i in range(L+1,R):
            cnt +=str(i).count(str(X))
            
        return cnt
