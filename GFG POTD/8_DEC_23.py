class Solution:
    def isPrime(self,a):
        if a==2: 
            return True
        if a==1: 
            return False
        for i in range(2,int(a**0.5)+1):
            if a%i==0: 
                return False
        return True
    def minNumber(self, arr,n):
        # code here
        total=sum(arr)
        preSum=total
        while not self.isPrime(total):
            total+=1
        return total-preSum
