class Solution:
    def missingNumber(self,array,n):
        arr_sum = sum(array)
        total_sum = n*(n+1)//2
        return  total_sum-arr_sum
