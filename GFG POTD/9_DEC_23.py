class Solution:
    def smithNum(self, n):
        if self.isPrime(n): 
            return 0
        ss = self.sumDigits(n)
        currSum = 0
        i = 2
        while i <= n and n > 1:
            if self.isPrime(i) == True:
                d = self.sumDigits(i)
                while n % i == 0:
                    currSum += d
                    n //= i
            i += 1
        return 1 if ss == currSum else 0
    def isPrime(self, n):
        i = 2
        while i * i <= n:
            if n % i == 0: 
                return False
            i += 1
        return n > 1
    def sumDigits(self, n):
        ss = 0
        while n > 0:
            ss += n % 10
            n //= 10
        return ss
